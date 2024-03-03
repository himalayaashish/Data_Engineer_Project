class MyApiException(Exception):
    def __init__(self, message="An error occurred"):
        self.message = message
        super().__init__(self.message)

    @staticmethod
    def handle_exception(response_status_code):
        if response_status_code == 404:
            return MyApiException("API endpoint not found or unavailable")
        else:
            return MyApiException(f"Error: {response_status_code}")

    @staticmethod
    def handle_validation_error(details):
        return MyApiException(f"Schema validation error: {details}")