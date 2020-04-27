import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('./cleaned_dataset.csv', encoding='utf-8')

for i in range(df.shape[0]):
    symptoms_string = df.iloc[i, 2]
    new_symptoms = symptoms_string.split(';')
    if len(new_symptoms)>9:
        new_symptoms = new_symptoms[:9]
    new_symptoms_string = ';'.join(new_symptoms)

    df.iloc[i, 2] = new_symptoms_string

df.to_csv('./trimmed_dataset.csv', encoding='utf-8', index=None)