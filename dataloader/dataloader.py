# -*- coding: utf-8 -*-
"""Data Loader"""

import jsonschema
import pymysql
import pandas as pd

import MyException
from configs.data_schema import SCHEMA, API_SCHEMA
import requests
from MyException.exceptions import MyApiException


class DataLoader:
    """Data Loader class"""

    @staticmethod
    def make_connection(conf):
        """Loads dataset from DB"""
        print("make_connection")
        con = pymysql.connect(host=conf.hostname, user=conf.username, passwd=conf.password, database=conf.database)
        return con

    @staticmethod
    def load_data(con):
        cursor = con.cursor()
        cursor.execute("SELECT * FROM sales")
        result = cursor.fetchall()
        df = pd.DataFrame(result, columns=["order_id", "customer_id", "product_id", "quantity", "price", "order_date"])
        con.commit()
        con.close()
        print("load_data")
        return df

    @staticmethod
    def validate_schema(df):
        try:
            # Convert DataFrame to list of dictionaries for validation
            data_list = df.to_dict(orient="records")
            jsonschema.validate(data_list, SCHEMA)
        except jsonschema.ValidationError as e:
            raise MyApiException.handle_validation_error(str(e))
        print("validate_schema")


class UserApiClient:

    @staticmethod
    def fetch_users_data(conf):
        """Fetch data from the API endpoint"""
        response = requests.get(conf.endpoint)

        if response.status_code == 200:
            users_data = response.json()
            return users_data
        else:
            raise MyApiException.handle_exception(response.status_code)

    @staticmethod
    def extract_relevant_fields(users_data):
        """Extract relevant fields from API response"""
        relevant_fields = []
        for user in users_data:
            user_info = {
                "id": user["id"],
                "name": user["name"],
                "username": user["username"],
                "email": user["email"],
                "lat": user["address"]["geo"]["lat"],
                "lng": user["address"]["geo"]["lng"],
            }
            relevant_fields.append(user_info)

        return relevant_fields

    @staticmethod
    def validate_api_schema(data_list):
        try:
            jsonschema.validate(data_list, API_SCHEMA)
        except jsonschema.ValidationError as e:
            raise MyApiException.handle_validation_error(str(e))
        print("User schema validation successful")


class WeatherApiClient:
    """Class for fetching weather information from OpenWeatherMap API."""

    @staticmethod
    def fetch_weather_data(conf,latitude, longitude):
        """Fetch weather data from the OpenWeatherMap API."""
        endpoint = conf.api
        params = {
            "lat": latitude,
            "lon": longitude,
            "appid": conf.key,
            "units": "metric"  # You can adjust the units as needed (e.g., "metric", "imperial", "standard")
        }

        response = requests.get(endpoint, params=params)

        if response.status_code == 200:
            weather_data = response.json()
            return weather_data
        else:
            raise MyApiException.handle_exception(response.status_code)