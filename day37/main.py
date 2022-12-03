import requests
from datetime import datetime

"""Working with pixela endpoint"""

# -----------------------These are the process involved in creating of user and graph in pixela-----------------#
""""
pixela_endP = "https://pixe.la/v1/users"
create_user_params = {
    "token": "PUT A TOKEN HERE",
    "username": "YOUR USERNAME",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endP, json=parameters)
response.raise_for_status()
print(response.text)

"""

USERNAME = "YOUR USERNAME"
TOKEN = "YOUR TOKEN"

HEADERS = {
    "X-USER-TOKEN": TOKEN
}

# Creating a graph definition
""""
graph_endP = f"https://pixe.la/v1/users/{USERNAME}/graphs"

create_graph_params = {
    "id": "graph1",
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

response = requests.post(url=graph_endP, json=create_graph_params, headers=headers)
print(response.text)
"""
GRAPH_ID = "graph1"
TODAY = datetime.now().strftime("%Y%m%d")

# posting a pixel
"""
post_a_pixel_endP = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"
value_to_graph_params = {
    "date": TODAY,
    "quantity": "8.5",
}

response = requests.post(url=post_a_pixel_endP, json=value_to_graph_params, headers=headers)
print(response.text)
"""

# updating the pixel for a chosen date
"""
update_a_pixel_endP = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"
update_a_pixel_params = {
    "quantity": "5.5",
}
response = requests.put(url=update_a_pixel_endP, json=update_a_pixel_params, headers=HEADERS)
print(response.text)
"""

# deleting pixel from the graph
delete_a_pixel_endP = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"

response = requests.delete(url=delete_a_pixel_endP, headers=HEADERS)
print(response.text)
