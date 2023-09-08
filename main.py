import requests
from requests import Response


def get_status(url: str) -> int:
    request: Response = requests.get(url)  # how do we annotate this?
    status_code: int = request.status_code
    return status_code


print(get_status("https://www.google.com"))
