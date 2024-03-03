# -*- coding: utf-8 -*-
from .base_model import BaseModel
from dataloader.dataloader import DataLoader, UserApiClient, WeatherApiClient
import jsonschema
from MyException.exceptions import MyApiException
import pandas as pd


class MyModel(BaseModel):
    """Unet Model Class"""

    def __init__(self, config):
        super().__init__(config)
        self.connection = None
        self.dataset = None
        self.schema = None
        self.users_data = None
        self.relevant_fields = None
        self.merged_df = pd.DataFrame()

    def make_connection(self):
        print("-----Connection Made -------")
        self.connection = DataLoader().make_connection(self.config.mysql)

    def load_data(self):
        """Loads data """
        self.dataset = DataLoader().load_data(self.connection)

    def validate_schema(self):
        print("----- Verify Data --------")
        try:
            DataLoader.validate_schema(self.dataset)
        except jsonschema.ValidationError as e:
            raise MyApiException.handle_validation_error(str(e))

    def load_api_data(self):
        self.users_data = UserApiClient().fetch_users_data(self.config.api_endpoint)
        # Extract relevant fields
        self.relevant_fields = UserApiClient().extract_relevant_fields(self.users_data)

        # Display the extracted data
        # for user_info in self.relevant_fields:
        #     print(user_info)

    def validate_api_schema(self):
        try:
            UserApiClient.validate_api_schema(self.relevant_fields)
        except jsonschema.ValidationError as e:
            raise MyApiException.handle_validation_error(str(e))
        print("----- Verify API Data --------")

    def merge_user_data(self):
        """Merge sales data with user data based on customer_id"""
        sales_df = pd.DataFrame(self.dataset)
        user_df = pd.DataFrame(self.users_data)

        # Merge based on customer_id
        self.merged_df = pd.merge(sales_df, user_df, how='left', left_on='customer_id', right_on='id',
                             suffixes=('_sale', '_user'))

        # Flatten nested dictionaries
        self.merged_df['street'] = self.merged_df['address'].apply(lambda x: x['street'] if pd.notna(x) else None)
        self.merged_df['suite'] = self.merged_df['address'].apply(lambda x: x['suite'] if pd.notna(x) else None)
        self.merged_df['city'] = self.merged_df['address'].apply(lambda x: x['city'] if pd.notna(x) else None)
        self.merged_df['zipcode'] = self.merged_df['address'].apply(lambda x: x['zipcode'] if pd.notna(x) else None)
        self.merged_df['geo'] = self.merged_df['address'].apply(lambda x: x['geo'] if pd.notna(x) else None)
        self.merged_df['geo_lat'] = self.merged_df['geo'].apply(lambda x: x['lat'] if pd.notna(x) else None)
        self.merged_df['geo_lng'] = self.merged_df['geo'].apply(lambda x: x['lng'] if pd.notna(x) else None)

        self.merged_df['name'] = self.merged_df['company'].apply(lambda x: x['name'] if pd.notna(x) else None)
        self.merged_df['catchPhrase'] = self.merged_df['company'].apply(lambda x: x['catchPhrase'] if pd.notna(x) else None)
        self.merged_df['bs'] = self.merged_df['company'].apply(lambda x: x['bs'] if pd.notna(x) else None)

        # Drop the original nested columns
        self.merged_df = self.merged_df.drop(['address'], axis=1)
        self.merged_df = self.merged_df.drop(['company'], axis=1)
        self.merged_df = self.merged_df.drop(['geo'], axis=1)

        self.merged_df.to_csv("AnalysisOutputResults/merged_df.csv", index=False)
        return self.merged_df.to_dict(orient='records')

    def merge_user_and_weather_data(self):
        """Merge sales data with user and weather data based on customer_id"""
        # Use the existing merge_user_data method to get the merged user data
        merged_user_data = self.merge_user_data()

        # Convert merged_user_data to a DataFrame
        merged_user_data = pd.DataFrame(merged_user_data)

        # Extract latitude and longitude from merged data
        locations = merged_user_data[['geo_lat', 'geo_lng']]

        # Fetch weather data for each location and merge it into the DataFrame
        for index, location in locations.iterrows():
            latitude, longitude = location['geo_lat'], location['geo_lng']

            try:
                weather_data = WeatherApiClient().fetch_weather_data(self.config.weather_api, latitude, longitude)
                # Include relevant weather information in the merged DataFrame
                merged_user_data.at[index, 'temperature'] = weather_data['main']['temp']
                merged_user_data.at[index, 'weather_conditions'] = weather_data['weather'][0]['description']

            except MyApiException as e:
                print(f"Error fetching weather data for location {latitude}, {longitude}: {str(e)}")

        # Save the final merged and weather data to a CSV file
        merged_user_data.to_csv("final_data.csv", index=False)

        return merged_user_data.to_dict(orient='records')