# -*- coding: utf-8 -*-
"""Model config in json format"""

SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "order_id": {"type": "integer"},
            "customer_id": {"type": "integer"},
            "product_id": {"type": "integer"},
            "quantity": {"type": "integer"},
            "price": {"type": "number"},
            "order_date": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$"}
        },
        "required": ["order_id", "customer_id", "product_id", "quantity", "price", "order_date"]
    }
}

# API Schema
API_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "username": {"type": "string"},
            "email": {"type": "string", "format": "email"},
            "lat": {"type": "string", "pattern": "^-?\d+\.\d+$"},
            "lng": {"type": "string", "pattern": "^-?\d+\.\d+$"}
        },
        "required": ["id", "name", "username", "email", "lat", "lng"]
    }
}
