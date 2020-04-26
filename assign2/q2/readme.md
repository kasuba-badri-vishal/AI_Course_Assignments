
### Dataset Construction
- The dataset (dataset.csv) has been scraped from the internet and preprocessed.
It contains diseases in the first row, number of cases of that disease in 2nd row and
symptoms in the third row.

- Treatments for the diseases have been found separately by using google knowledge graph api. The file cleaned_dataset.csv contains cleaned data along with the treatments for corresponding diseases.

- The final dataset contains a total of 127 diseases, symptoms and their treatments.

### Disease-Symptom Knowledge Graph Construction
- The file kg.py contains python script that uses the data collected to form
a knowledge graph using the python module networkx. 
- Graphs for less number of diseases (5 and 10) has been plotted to easily show the knowledge graph.
- Knowledge graph for the whole set has also been plotted. 
- They are also saved as pickle files. plots are saved in graphs/ folder.

<img src='./graphs/Knowledge_Graph_5_diseases.png' style="height:400px; width:400px;">
<img src='./graphs/Knowledge_Graph_all_diseases.png' style="height:400px; width:400px;">

### QA Diagnostic System
- The Diagnostic system takes a list of symptoms seperated by commas.
- First it tries to use the knowledge graph to find exact matching disease with the given symptoms. This has been done by finding the neighbors of a disease and matching them with the symptoms the user has given as input.
- If no exact match is found, it outputs the next best match according to the number of symptoms matched.




