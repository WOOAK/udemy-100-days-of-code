import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "90dygd752fsT87wds"
USERNAME = "akwoo39"
today = datetime.now()
today_date = today.strftime("%Y%m%d")

user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

# create a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id":"pythoncourse",
    "name":"Time taken to attend Python courses",
    "unit":"minute",
    "type":"int",
    "color":"sora"
}

# response = requests.post(url=graph_endpoint,json=graph_config,headers=header)

header = {
    "X-USER-TOKEN":TOKEN
}

# update profile picture
profile_endpoint = f"https://pixe.la/@{USERNAME}"
user_profile_params = {
    "displayName":"Ay Kuan Woo",
    "gravatarIconEmail":"aykuan1992@gmail.com",
    "title":"Reenie's lover",
    "timezone":"Asia/Kuala_Lumpur"
}

# response = requests.put(url=profile_endpoint,json=user_profile_params,headers=header)

# post pixel to date
post_pixel_params = {
    "date":today_date,
    "quantity":"90"
}
post_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/pythoncourse"
response = requests.post(url=post_pixel_endpoint,json=post_pixel_params,headers=header)

# update graph
update_graph_params = {
    "timezone":"Asia/Kuala_Lumpur"
}
# response = requests.put(url=post_pixel_endpoint,json=update_graph_params,headers=header)

# delete a pixel from date
delete_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/pythoncourse/20210310"
# response = requests.delete(url=delete_pixel_endpoint,headers=header)

# get a graph stat

graph_stat_endoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/pythoncourse/stats"
# response = requests.get(url=graph_stat_endoint)

# get a graph svg ()
graph_svg_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/pythoncourse"
graph_svg_params = {
    "date":today_date
}
# response = requests.get(url=graph_svg_endpoint,json=graph_svg_params)

print(response.text)