import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx

graph = dict()

df = pd.read_csv('cleaned_dataset2.csv', encoding='utf-8')

# df = df.head(5)

edge_list = []

colors = []
diseases = []
symptoms = []

for i in range(df.shape[0]):
    for symptom in df.iloc[i, 2].split(';'):
        edge_list.append((symptom, df.iloc[i, 0]))
        diseases.append(df.iloc[i, 0])
        symptoms.append(symptom)

G = nx.DiGraph()

G.add_edges_from(edge_list)

nx.write_gpickle(G, f"kg_graph_{df.shape[0]}.pkl")

# for node in G.nodes:
#     if node in diseases:
#         colors.append('skyblue')
#     else:
#         colors.append('#FF6347')

# plt.figure(figsize=(14,14))
# plt.title("Diseases and Symptoms Knowledge Graph")
# # pos = nx.spring_layout(G)
# # pos = nx.random_layout(G)
# # pos = nx.bipartite_layout(G)
# pos = nx.bipartite_layout(G,symptoms)

# options = {
#     # 'node_size': 20,
#     # 'node_size': 1000,
#     'node_size': 200,
#     'width': 0.4,
#     'font_size':8,
#     'alpha':0.75,
#     'edge_color': '#555555',
#     'node_color':colors,
#     # 'with_labels':False,
#     'with_labels':True,
#     'pos':pos,
#     # 'label':"Disease"
# }
# nx.draw(G, **options)
# plt.savefig(f"graphs/Knowledge_Graph_{df.shape[0]}_diseases.png")
# plt.show()