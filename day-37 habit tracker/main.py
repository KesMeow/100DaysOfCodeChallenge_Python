import requests
from datetime import datetime

from requests.api import delete
pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "YOUR_USERNAME"
TOKEN = "YOUR_TOKEN"
GRAPH_ID = "YOUR_GRAPH"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "LC questions",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()
print(today)

formatted_today = today.strftime("%Y%m%d")
print(formatted_today)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data = {
    "date": formatted_today,
    "quantity": "10.00",
}

# requests.post(url=pixel_creation_endpoint, json = pixel_data, headers=headers)
# print(response.text)

# Update a Pixel
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_today}"

new_pixel_data = {
    "quantity": "5"
}

response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)

# Delete a Pixel
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_today}"

response = requests.delete(url=delete, headers=headers)
print(response.text)