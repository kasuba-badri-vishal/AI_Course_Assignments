import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

graph = dict()

df = pd.read_csv('cleaned_dataset2.csv', encoding='utf-8')

# print(df.head())

edge_list = []

graph = {}

for i in range(df.shape[0]):
    for symptom in df.iloc[i, 2].split(';'):
        edge_list.append((df.iloc[i, 0], symptom))
        if graph.get(symptom)==None:
            graph[symptom] = [df.iloc[i, 0]]
        graph[symptom].append(df.iloc[i, 0])

def find_disease(user_symptoms):
    common_counts = []
    for i in range(df.shape[0]):
        symptoms = df.iloc[i, 2].split(';')
        count = 0
        for x in user_symptoms:
            if x in symptoms:
                count += 1
        common_counts.append(count)
        
    return common_counts




# while True:
#     ans = input("List your symptoms seperated by commas: ")
#     user_symptoms = ans.split(',')
    
#     find_disease(user_symptoms)

#     print(f"Diagnosis: {}")