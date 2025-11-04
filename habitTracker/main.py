from datetime import date, datetime, timedelta
import requests

#create account at PIXELA
# PIXELA_CREATE_USER_ENDPOINT = "https://pixe.la/v1/users"

# create_user_parameters = {
#     "token": "43t4j09jdaae22r",
#     "username": 'marsatpixela',
#     "agreeTermsOfService":"yes",
#     "notMinor":"yes"
# }

# response = requests.post(url=PIXELA_CREATE_USER_ENDPOINT, json=create_user_parameters)
# print(response.text)

####################################################################################################
#create graph at PIXELA
# USERNAME = "marsatpixela"
# TOKEN = "43t4j09jdaae22r"
# graphDefinitionEndpoint = "https://pixe.la/v1/users"
# graph_endpoint = f"{graphDefinitionEndpoint}/{USERNAME}/graphs"
# graph_creation_params = {
#     "id": 'graph1',
#     "name": "Cycling graph",
#     "unit":"km",
#     "type":"float",
#     "color": "ajisai"
# }
# headers = {
#     "X-USER-TOKEN": TOKEN
# }

# response = requests.post(url=graph_endpoint, json=graph_creation_params, headers=headers)
# print(response.text)

####################################################################################################
# insert pixel in graph - https://pixe.la/v1/users/marsatpixela/graphs/graph1.html

# USERNAME = "marsatpixela"
# TOKEN = "43t4j09jdaae22r"
# GRAPHID = "graph1"
# graphDefinitionEndpoint = "https://pixe.la/v1/users"
# graph_endpoint = f"{graphDefinitionEndpoint}/{USERNAME}/graphs/{GRAPHID}"
# today = datetime.now()
# pixel_insertion_params = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": '1'
# }
# headers = {
#     "X-USER-TOKEN": TOKEN
# }

# response = requests.post(url=graph_endpoint, json=pixel_insertion_params, headers=headers)
# print(response.text)

####################################################################################################
# Modify quantity in graph at specified date and time
# https://pixe.la/v1/users/marsatpixela/graphs/graph1.html
# USERNAME = "marsatpixela"
# TOKEN = "43t4j09jdaae22r"
# GRAPHID = "graph1"
# graphDefinitionEndpoint = "https://pixe.la/v1/users"
# graph_endpoint = f"{graphDefinitionEndpoint}/{USERNAME}/graphs/{GRAPHID}/20251104"
# pixel_mod_params = {
#     "quantity": '50'
# }
# headers = {
#     "X-USER-TOKEN": TOKEN
# }

# response = requests.put(url=graph_endpoint, json=pixel_mod_params, headers=headers)
# print(response.text)

####################################################################################################
# Delete pixel entry
# https://pixe.la/v1/users/marsatpixela/graphs/graph1.html
USERNAME = "marsatpixela"
TOKEN = "43t4j09jdaae22r"
GRAPHID = "graph1"
graphDefinitionEndpoint = "https://pixe.la/v1/users"
headers = {
    "X-USER-TOKEN": TOKEN
}
graph_endpoint = f"{graphDefinitionEndpoint}/{USERNAME}/graphs/{GRAPHID}/20251104"
response = requests.delete(url=graph_endpoint, headers=headers)
print(response.text)