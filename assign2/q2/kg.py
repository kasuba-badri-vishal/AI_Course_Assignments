import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx

df = pd.read_csv('cleaned_dataset.csv', encoding='utf-8')

# df = df.sample(8)

edge_list = []

colors = []
diseases = dict()
symptoms = dict()

for i in range(df.shape[0]):
    for symptom in df.iloc[i, 2].split(';'):
        edge_list.append((symptom, df.iloc[i, 0]))
        diseases[df.iloc[i, 0]] = 1
        symptoms[symptom] = 1

G = nx.DiGraph()

G.add_edges_from(edge_list)

nx.write_gpickle(G, f"pickles/kg_graph_{df.shape[0]}.pkl")

for node in G.nodes:
    if node in diseases:
        colors.append('skyblue')
    else:
        colors.append('#FF6347')

# plt.figure(figsize=(14,14))
plt.figure(figsize=(25,25))
plt.title("Diseases and Symptoms Knowledge Graph")
# pos = nx.spring_layout(G)
# pos = nx.random_layout(G)
pos = nx.bipartite_layout(G,list(symptoms.keys()))

options = {
    # 'node_size': 50,
    # 'node_size': 1000,
    'node_size': 200,
    'width': 0.4,
    # 'width': 0.15,
    'font_size':7,
    'alpha':0.65,
    'edge_color': '#555555',
    'node_color':colors,
    # 'with_labels':False,
    'with_labels':True,
    'pos':pos,
    # 'label':"Disease"
}
nx.draw(G, **options)
plt.savefig(f"graphs/Knowledge_Graph_{df.shape[0]}_diseases.png")
# plt.savefig(f"graphs/Knowledge_Graph_all_diseases_bipartite.png")
plt.show()