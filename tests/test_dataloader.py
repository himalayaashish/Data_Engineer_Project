import pytest
import pandas as pd
import jsonschema
from unittest.mock import Mock, patch
from dataloader.dataloader import DataLoader, UserApiClient, WeatherApiClient
from MyException.exceptions import MyApiException
from configs.data_schema import SCHEMA, API_SCHEMA


@pytest.fixture
def mock_sales_data():
    return [
        (2334, 5, 40, 3, 35.6, '2022-06-21'),
        (6228, 8, 13, 7, 36.52, '2023-03-08'),
        # Add more sample data as needed
    ]


@pytest.fixture
def mock_users_data():
    return [
        {"id": 1, "name": "User 1", "username": "user1", "email": "user1@example.com", "address": {"geo": {"lat": 1, "lng": 2}}},
        {"id": 2, "name": "User 2", "username": "user2", "email": "user2@example.com", "address": {"geo": {"lat": 3, "lng": 4}}},
        # Add more sample data as needed
    ]


@pytest.fixture
def mock_weather_data():
    return {
        "main": {"temp": 20},
        "weather": [{"description": "Clear sky"}]
    }


class TestDataLoader:

    @staticmethod
    @patch('dataloader.dataloader.pymysql.connect')
    def test_make_connection(mock_connect, mock_sales_data):
        conf_mock = Mock(hostname="host", username="user", password="pass", database="db")
        mock_connect.return_value.cursor.return_value.fetchall.return_value = mock_sales_data
        DataLoader.make_connection(conf_mock)
        mock_connect.assert_called_once_with(host="host", user="user", passwd="pass", database="db")

    @staticmethod
    @patch('dataloader.dataloader.pymysql.connect')
    def test_load_data(mock_connect, mock_sales_data):
        conf_mock = Mock(hostname="host", username="user", password="pass", database="db")
        con_mock = Mock()
        cursor_mock = con_mock.cursor.return_value
        cursor_mock.fetchall.return_value = mock_sales_data

        mock_connect.return_value = con_mock
        data = DataLoader.load_data(con_mock)

        cursor_mock.execute.assert_called_once_with("SELECT * FROM sales")
        cursor_mock.fetchall.assert_called_once()
        con_mock.commit.assert_called_once()
        con_mock.close.assert_called_once()
        assert isinstance(data, pd.DataFrame)

    @staticmethod
    @patch('dataloader.dataloader.jsonschema.validate')
    def test_validate_schema_valid(mock_validate, mock_sales_data):
        df = pd.DataFrame(mock_sales_data, columns=["order_id", "customer_id", "product_id", "quantity", "price", "order_date"])
        DataLoader.validate_schema(df)
        mock_validate.assert_called_once_with(df.to_dict(orient="records"), SCHEMA)

    @staticmethod
    @patch('dataloader.dataloader.jsonschema.validate', side_effect=jsonschema.ValidationError("Invalid schema"))
    def test_validate_schema_invalid(mock_validate, mock_sales_data):
        df = pd.DataFrame(mock_sales_data, columns=["order_id", "customer_id", "product_id", "quantity", "price", "order_date"])
        invalid_schema_data = df.copy()
        invalid_schema_data["order_id"] = "invalid"
        with pytest.raises(MyApiException):
            DataLoader.validate_schema(invalid_schema_data)


class TestUserApiClient:

    @staticmethod
    @patch('dataloader.dataloader.requests.get')
    def test_fetch_users_data(mock_get, mock_users_data):
        conf_mock = Mock(endpoint="https://api.example.com/users")
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_users_data
        data = UserApiClient.fetch_users_data(conf_mock)

        mock_get.assert_called_once_with("https://api.example.com/users")
        assert data == mock_users_data

    @staticmethod
    @patch('dataloader.dataloader.requests.get', return_value=Mock(status_code=404))
    def test_fetch_users_data_error(mock_get, mock_users_data):
        conf_mock = Mock(endpoint="https://api.example.com/users")
        with pytest.raises(MyApiException, match="API endpoint not found or unavailable"):
            UserApiClient.fetch_users_data(conf_mock)

        mock_get.assert_called_once_with("https://api.example.com/users")

    @staticmethod
    def test_extract_relevant_fields(mock_users_data):
        data = UserApiClient.extract_relevant_fields(mock_users_data)
        assert data == [
            {"id": 1, "name": "User 1", "username": "user1", "email": "user1@example.com", "lat": 1, "lng": 2},
            {"id": 2, "name": "User 2", "username": "user2", "email": "user2@example.com", "lat": 3, "lng": 4}
        ]

    @staticmethod
    @patch('dataloader.dataloader.jsonschema.validate')
    def test_validate_api_schema_valid(mock_validate, mock_users_data):
        UserApiClient.validate_api_schema(mock_users_data)
        mock_validate.assert_called_once_with(mock_users_data, API_SCHEMA)

    @staticmethod
    @patch('dataloader.dataloader.jsonschema.validate', side_effect=jsonschema.ValidationError("Invalid schema"))
    def test_validate_api_schema_invalid(mock_validate, mock_users_data):
        invalid_api_data = mock_users_data.copy()
        invalid_api_data[0]["id"] = "invalid"
        with pytest.raises(MyApiException):
            UserApiClient.validate_api_schema(invalid_api_data)


class TestWeatherApiClient:

    @staticmethod
    @patch('dataloader.dataloader.requests.get')
    def test_fetch_weather_data(mock_get, mock_weather_data):
        conf_mock = Mock(api="https://api.openweathermap.org/data/2.5/weather", key="apikey")
        latitude, longitude = 1, 2
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_weather_data
        data = WeatherApiClient.fetch_weather_data(conf_mock, latitude, longitude)

        mock_get.assert_called_once_with(
            "https://api.openweathermap.org/data/2.5/weather",
            params={"lat": 1, "lon": 2, "appid": "apikey", "units": "metric"}
        )
        assert data == mock_weather_data

    @staticmethod
    @patch('dataloader.dataloader.requests.get', return_value=Mock(status_code=404))
    def test_fetch_weather_data_error(mock_get, mock_weather_data):
        conf_mock = Mock(api="https://api.openweathermap.org/data/2.5/weather", key="apikey")
        latitude, longitude = 1, 2
        with pytest.raises(MyApiException):
            WeatherApiClient.fetch_weather_data(conf_mock, latitude, longitude)

        mock_get.assert_called_once_with(
            "https://api.openweathermap.org/data/2.5/weather",
            params={"lat": 1, "lon": 2, "appid": "apikey", "units": "metric"}
        )
