import requests

API_KEY = "YOUR_API_KEY_HERE"


def generate_random_password(
    length: int, hasDigits: bool, hasSpecial: bool, hasUppercase: bool
):
    """
    Make a GET request to the Randommer API to generate a random password.

    This function should:
    - Send a GET request to: https://randommer.io/api/Password
    - Include the API key in the X-Api-Key header
    - params = {
        "length": "The length field is required.",
        "hasDigits": "The hasDigits field is required.",
        "hasSpecial": "The hasSpecial field is required.",
        "hasUppercase": "The hasUppercase field is required."
    },
    - Print the generated password from the response
    """
    pass
