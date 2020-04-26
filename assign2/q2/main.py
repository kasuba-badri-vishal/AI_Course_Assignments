import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from difflib import get_close_matches

df = pd.read_csv('cleaned_dataset.csv', encoding='utf-8')

edge_list = []

diseases = {}
symptoms = {}

for i in range(df.shape[0]):
    for symptom in df.iloc[i, 2].split(';'):
        edge_list.append((symptom, df.iloc[i, 0]))
        diseases[df.iloc[i, 0]] = 1
        symptoms[symptom] = 1

G = nx.DiGraph()

G.add_edges_from(edge_list)
G1 = G.reverse()

def filter_symptoms(symptom):
    return get_close_matches(symptom, symptoms)

def count_common_items(a, b):
    count = 0
    for x in a:
        if x in b:
            count += 1

    return count

def find_disease(user_symptoms):
    common_counts = {}
    exact_match = ""
    for d in diseases.keys():
        common_counts[d] = count_common_items(G1.neighbors(d), user_symptoms)
        if len(user_symptoms)==len(common_counts):
            exact_match = d
    return common_counts, exact_match

while True:
    ans = input("\n\nList your symptoms seperated by commas: ")
    user_symptoms = ans.split(',')
    user_symptoms = [x.strip(' ').strip("'") for x in user_symptoms]
    
    common_counts, exact_match = find_disease(user_symptoms)

    results = sorted(list(common_counts.items()), key = lambda x:x[1],reverse=True)

    filtered_results = []
    for x in results:
        if x[1]>0: filtered_results.append(x)

    # print(f"Diagnosis: {filtered_results}")
    # for x,y in filtered_results:
    #     print(f"{x}: {y}")

    if exact_match!="":
        print(f"\nDiagnosis: ", exact_match)
        print(f"\nfound using rule: ")
        print("IF", ' ^ '.join(G1.neighbors(exact_match)), "THEN", exact_match)
        
        print("\nTREATMENT: ", df[df.iloc[:, 0]==exact_match].iloc[0,3])
    else:
        print("No exact matches found")