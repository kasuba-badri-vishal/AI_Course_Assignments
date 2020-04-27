from pyke import knowledge_base, knowledge_engine, ask_tty
import pandas as pd
from create_rule_file import create_bc_rules

RULE_FILE = "bc_rules"

def check_disease(disease, i):
    if i>=df.shape[0]:
        return
    try:
        vals, plans = my_engine.prove_1_goal(f"{RULE_FILE}.has_disease{i}()")
        print(f"\nDiagnosis: You could have {disease}.")
        print(f"\nTREATMENT: {df.iloc[i, 3]}\n")
        return vals, plans
    except:
        if i+1<df.shape[0]:
            check_disease(df.iloc[i+1, 0], i+1)
        else:
            pass

if __name__=="__main__":
    df = pd.read_csv('./trimmed_dataset.csv', encoding='utf-8')
    RULE_FILE = create_bc_rules(df)
    
    my_engine = knowledge_engine.engine('./knowledgebase')
    my_engine.ask_module = ask_tty
    my_engine.reset()


    my_engine.activate(RULE_FILE)

    check_disease(df.iloc[0,0],0)