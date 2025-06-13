import requests

API_KEY = "YOUR_API_KEY_HERE"


def get_random_name(nameType:str, quantity: int):
    """
    Make a GET request to the Randommer API to get a random name.

    This function should:
    - Send a GET request to: https://randommer.io/api/Name
    - With parameter nameType and quantity
    - nameType = one of these ("firstname" "surname" "fullname")
    - quantity = number of names
    - Include the API key in the X-Api-Key header
    - Print the random name from the response
    """
