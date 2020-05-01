import pandas as pd
import numpy as np
import requests
import gmplot

# class Node:
#     def __init__(self):
#         self.g = 0
#         self.h = 0
#         self.f = 0
#         self.parent = -1


df = pd.read_csv("./places_H.csv")
print(df.head(5))

place_hash = {}
for i in range(len(df["Place"])):
    place_hash[df["Place"][i]] = i


graph = {}
edges_df = pd.read_csv("./edges_distance.csv")

for i in range(edges_df.shape[0]):
    if place_hash[edges_df["Source"][i]] not in graph.keys():
        graph[place_hash[edges_df["Source"][i]]] = []
    if place_hash[edges_df["Destination"][i]] not in graph.keys():
        graph[place_hash[edges_df["Destination"][i]]]=[]
    
    graph[place_hash[edges_df["Source"][i]]].append(place_hash[edges_df["Destination"][i]])
    graph[place_hash[edges_df["Destination"][i]]].append(place_hash[edges_df["Source"][i]])

for i in range(len(graph.keys())):
    print(i," ",graph[i])


# Undirected Graph is form of adjacency list with no weights
# Latitudes and longitudes are obtained from previous places file
source = place_hash["BITS Hyderabad"]
destination = place_hash["RGIA"]

distance_dict = {}
for i in range(edges_df.shape[0]):
    # any edge is place_hash[]
    edge_tup = (place_hash[edges_df["Source"][i]],place_hash[edges_df["Destination"][i]]) 
    print(edge_tup)
    distance_dict[edge_tup] = edges_df["Forward"][i]
    distance_dict[(edge_tup[1],edge_tup[0])] = edges_df["Backward"][i]

# print(len(distance_dict.keys()))
for i in distance_dict.keys():
    print(i)
    print(distance_dict[i])

# Now i have whole graph with me
# whole distances between edges for g and h
# and they are hashed so every edge is accessible easily

open_dict= {} #visited[i]=1
closed_dict= {} #visited[i]=0
nodes_dict = []
for i in range(df.shape[0]):
    object_node = {}
    object_node["g"]=np.inf
    object_node["h"]=df["H"][i]
    object_node["f"]=np.inf
    object_node["parent"]=-1
    nodes_dict.append(object_node)

nodes_dict[source]["g"] = 0
nodes_dict[source]["f"] = nodes_dict[source]["g"]+nodes_dict[source]["h"]

# keys of this are source numbers ode numbers 
# values are f whole distance values
open_dict[source]=nodes_dict[source]["f"]

print(sorted(open_dict.items()))
print(sorted(open_dict.items(), key = lambda kv:(kv[1], kv[0])))   

while len(open_dict)!=0:
    curr_node = sorted(open_dict.items(), key = lambda kv:(kv[1], kv[0]))[0]
    print(curr_node)
    if curr_node[0] == destination:
        print("PATH FOUND")
        break

    for node in graph[curr_node[0]]:
        print(node)
        if node not in closed_dict.keys():
            if node not in open_dict.keys():
                nodes_dict[node]["parent"] = curr_node[0]
                nodes_dict[node]["g"] = nodes_dict[curr_node[0]]["g"]+distance_dict[(curr_node[0],node)]
                nodes_dict[node]["f"] = nodes_dict[node]["g"]+nodes_dict[node]["h"]

                open_dict[node] = nodes_dict[node]["f"]
            else:
                if nodes_dict[node]["g"] > nodes_dict[curr_node[0]]["g"]+distance_dict[(curr_node[0],node)]:
                    nodes_dict[node]["parent"] = curr_node[0]
                    nodes_dict[node]["g"] = nodes_dict[curr_node[0]]["g"]+distance_dict[(curr_node[0],node)]
                    nodes_dict[node]["f"] = nodes_dict[node]["g"] + nodes_dict[node]["f"]

                    open_dict[node] = nodes_dict[node]["f"]

    
    closed_dict[curr_node[0]] = curr_node[1]
    del open_dict[curr_node[0]]

    print(open_dict)
    print(closed_dict)

    # open_list.pop(0)

path = []
curr_node = destination
while(nodes_dict[curr_node]["parent"]!=-1):
    path.append(curr_node)
    # print(curr_node)
    curr_node = nodes_dict[curr_node]["parent"]
# print(curr_node)
path.append(curr_node)
path.reverse()



def find_paths(source): #only for class functions self is required
    global destination,found_path,visited,allpath,num
    num+=1
    # if(num>1000):
    #     return
    visited[source] = 1
    allpath.append(source)
    
    if source == destination:
        # print(path)
        new_path = []
        for i in range(len(allpath)):
            new_path.append(allpath[i])
        found_path.append(new_path)
    else:
        for i in graph[source]:
            # print(i)
            if visited[i]==0:
                find_paths(i)
            if(source==40):
                print(len(found_path))
    
    allpath.pop(len(allpath)-1)
    visited[source] = 0

num = 0
found_path = []
visited = {} #global dictionary
for i in range(df.shape[0]):
    visited[i] = 0
path_length = 0
allpath = []
find_paths(source)



print(len(found_path))



path_lat = []
path_lon = []
for i in range(len(path)):
    path_lat.append(df["Latitude"][path[i]])
    path_lon.append(df["Longitude"][path[i]])
    print(df["Place"][path[i]]," ",path_lat[i]," ",path_lon[i])

gmap = gmplot.GoogleMapPlotter(np.mean(path_lat),np.mean(path_lon), 13)
gmap.plot(path_lat,path_lon, 'cornflowerblue', edge_width=10)

gmap.scatter(path_lat, path_lon, 'yellow', size=400, marker=False)


gmap.marker(path_lat[0], path_lon[0], 'green')
gmap.marker(path_lat[len(path_lat)-1], path_lon[len(path_lat)-1], 'cornflowerblue')


for i in range(len(found_path)):
    if i%1000==0:
        allpath_lat = []
        allpath_lon = []
        for j in range(len(found_path[i])):
            allpath_lat.append(df["Latitude"][found_path[i][j]])
            allpath_lon.append(df["Longitude"][found_path[i][j]]) 
        # gmap = gmplot.GoogleMapPlotter(np.mean(allpath_lat),np.mean(allpath_lon), 13)
        # gmap.plot(allpath_lat,allpath_lon, 'cornflowerblue', edge_width=10) 
        gmap.scatter(allpath_lat, allpath_lon, 'yellow', size=400, marker=False)


gmap.draw("final_path.html")