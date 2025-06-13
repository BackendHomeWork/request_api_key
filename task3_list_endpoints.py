import requests

API_KEY = "YOUR_API_KEY_HERE"


def list_available_endpoints(length: int, hasDigits: bool, hasSpecial: bool, hasUppercase: bool):
    """
    Make a GET request to discover all available endpoints on Randommer API.

    This function should:
    - Send a GET request to: https://randommer.io/api/AvailableEndpoints
    - Include the API key in the X-Api-Key header
    - params = {
        "length": "The length field is required.",
        "hasDigits": "The hasDigits field is required.",
        "hasSpecial": "The hasSpecial field is required.",
        "hasUppercase": "The hasUppercase field is required."
    },
    - Print the list of available endpoints from the response
    """
    pass
