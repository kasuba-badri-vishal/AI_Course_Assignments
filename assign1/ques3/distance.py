import requests
import pandas as pd
import numpy as np
import json

df = pd.read_csv("./places.csv")
print(df.head(5))

place_hash = {}
for i in range(len(df["Place"])):
    place_hash[df["Place"][i]] = i

edges_df = pd.read_csv("./edges.csv")
forward = []
backward = []
# for i in range(edges_df.shape[0]):
#     # edge is place_hash[edges_df.iloc[i]["Source"]] and place_hash[edges_df.iloc[i]["Destination"]]
#     source = [df["Latitude"][place_hash[edges_df.iloc[i]["Source"]]],df["Longitude"][place_hash[edges_df.iloc[i]["Source"]]]]
#     destination = [df["Latitude"][place_hash[edges_df.iloc[i]["Destination"]]],df["Longitude"][place_hash[edges_df.iloc[i]["Destination"]]]]
#     # print(source)
#     # print(destination)
#     # print("\n")
#     URL = 'https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins= {},{}&destinations={},{}&travelMode=driving&key=Al723th9c0wqHtSxpbHHI-LXgAmHevtKxeNRg1s_30wKullrd0LOguIbvbzofXj5'.format(source[0],source[1],destination[0],destination[1])
#     # print(URL)
#     x = requests.get(URL)
#     x = json.loads(x.text)
#     # print(type(x))
#     dist_forward = x["resourceSets"][0]["resources"][0]["results"][0]["travelDistance"]
#     forward.append(dist_forward)
#     print(dist_forward)

# for i in range(edges_df.shape[0]):
#     # edge is place_hash[edges_df.iloc[i]["Source"]] and place_hash[edges_df.iloc[i]["Destination"]]
#     destination = [df["Latitude"][place_hash[edges_df.iloc[i]["Source"]]],df["Longitude"][place_hash[edges_df.iloc[i]["Source"]]]]
#     source = [df["Latitude"][place_hash[edges_df.iloc[i]["Destination"]]],df["Longitude"][place_hash[edges_df.iloc[i]["Destination"]]]]
#     # print(source)
#     # print(destination)
#     # print("\n")
#     URL = 'https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins= {},{}&destinations={},{}&travelMode=driving&key=Al723th9c0wqHtSxpbHHI-LXgAmHevtKxeNRg1s_30wKullrd0LOguIbvbzofXj5'.format(source[0],source[1],destination[0],destination[1])
#     # print(URL)
#     x = requests.get(URL)
#     x = json.loads(x.text)
#     # print(type(x))
#     dist_backward = x["resourceSets"][0]["resources"][0]["results"][0]["travelDistance"]
#     backward.append(dist_backward)
#     print(dist_backward)

# edges_df["Forward"] = forward
# edges_df["Backward"] = backward

# edges_df.to_csv('edges_distance.csv')

H_distace = []
for i in range(df.shape[0]):
    source = [df["Latitude"][i],df["Longitude"][i]]
    destination = [df["Latitude"][place_hash["RGIA"]],df["Longitude"][place_hash["RGIA"]]]
    URL = 'https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins= {},{}&destinations={},{}&travelMode=driving&key=Al723th9c0wqHtSxpbHHI-LXgAmHevtKxeNRg1s_30wKullrd0LOguIbvbzofXj5'.format(source[0],source[1],destination[0],destination[1])
    x = requests.get(URL)
    x = json.loads(x.text)
    # print(type(x))
    h = x["resourceSets"][0]["resources"][0]["results"][0]["travelDistance"]
    print(h)
    H_distace.append(h)

df["H"] = H_distace
df.to_csv("places_H.csv")