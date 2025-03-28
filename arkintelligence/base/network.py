import requests


def send_request(url, headers, data):
    """
    Send a request to the specified URL with the given headers and data.

    Args:
        url (str): The URL to send the request to.
        headers (dict): The headers to include in the request.
        data (dict): The data to include in the request.

    Returns:
        dict: The response from the server.
    """
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None