import requests
import datetime as dt
USERNAME = "gorkem"
TOKEN = "abcd1234$$?41"
pixela_endpoint = "https://pixe.la/v1/users"

headers = {
    "X-USER-TOKEN": TOKEN
}

# user_params = {
#     # we created this token
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

GRAPH_ID = "graph1"
# graph_params = {
#     "id": GRAPH_ID,
#     "name": "Cycling graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "sora",
#
# }

# graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(graph_response.text)

date = dt.datetime.today().date().strftime("%Y%m%d")
requests_params = {
    "date": date,
    "quantity": "9.74",
}
pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

requests_response = requests.post(url=pixel_creation_endpoint, json=requests_params, headers=headers)
print(requests_response)

# update_graph_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
# update_graph_params = {
#     "color": "ajisai",
# }
# update_response = requests.put(url=update_graph_endpoint, json=update_graph_params, headers=headers)
# print(update_response)

# delete_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{date}"
# delete_response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(delete_response.text)