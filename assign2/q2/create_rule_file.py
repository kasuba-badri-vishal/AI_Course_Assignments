import pandas as pd

def create_bc_rules(df):
    # df = pd.read_csv('./trimmed_dataset.csv', encoding='utf-8')

    with open("./knowledgebase/bc_rules.krb", 'w+') as f:
        for i in range(df.shape[0]):
            disease = df.iloc[i, 0]
            f.write(f'''has_disease{i}\n\tuse has_disease{i}()\n\twhen\n''')
            for symptom in df.iloc[i, 2].split(';'):
                f.write(f'''\t\tquestions.have_symptom("{symptom}", True)\n''')

            f.write("\n")
    return "bc_rules"

# with open("fc_rules.krb", 'w+') as f:
#     for i in range(df.shape[0]):
#         disease = df.iloc[i, 0]
#         f.write(f'''has_disease{i}\n\tforeach\n''')
#         for symptom in df.iloc[i, 2].split(';'):
#             f.write(f"\t\tquestions.have_symptom('{symptom}', True)\n")
        
#         f.write("\tassert\n")
#         f.write(f"\t\tfacts.has_disease{i}()\n\n")

