# -*- coding: utf-8 -*-
"""Model config in json format"""

CFG = {
    "mysql": {
        "hostname": "localhost",
        "username": "root",
        "password": "Hima@2023",
        "port": 3306,
        "database": "AIQ_SALES_DB",
        "load_with_info": True
    },
    "api_endpoint": {
        "endpoint": "https://jsonplaceholder.typicode.com/users"
    },
    "weather_api": {
        "api": "https://api.openweathermap.org/data/2.5/weather?",
        "key": "05e6c7119601d07f9075f52772839de4"

    }
}
