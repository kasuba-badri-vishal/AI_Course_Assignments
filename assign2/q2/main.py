from pyke import knowledge_base, knowledge_engine, ask_tty
import pandas as pd
from create_rule_file import create_bc_rules
import shutil

RULE_FILE = "bc_rules"

def check_disease(disease, i):
    if i>=df.shape[0]:
        return
    try:
        vals, plans = my_engine.prove_1_goal(f"{RULE_FILE}.has_disease{i}()")
        print(f"\nDiagnosis: You could have {disease}.")
        print(f"\nTREATMENT: {df.iloc[i, 3]}\n")
        print(f'''Rule used: IF {" ^ ".join(df.iloc[i,2].split(';'))} THEN {disease}''')

        return vals, plans
    except knowledge_engine.CanNotProve:
        if i+1<df.shape[0]:
            check_disease(df.iloc[i+1, 0], i+1)
        else:
            pass

if __name__=="__main__":
    df = pd.read_csv('./trimmed_dataset.csv', encoding='utf-8')
    RULE_FILE = create_bc_rules(df)
    try:
        shutil.rmtree('./compiled_krb')
    except:
        pass
    
    my_engine = knowledge_engine.engine('./knowledgebase')
    my_engine.ask_module = ask_tty
    my_engine.reset()

    print('''\n\n*****Welcome to Medical Diagnosis System******
    I am your personal Diagnosis Expert System. Please answer the following questions''')

    my_engine.activate('ask_rules')
    my_engine.activate(RULE_FILE)

    vals, plans = my_engine.prove_1_goal(f"ask_rules.get_name($name)")
    print(vals['name'])
    
    # vals, plans = my_engine.prove_1_goal(f"ask_rules.get_age($age)")
    # print(vals['age'])

    check_disease(df.iloc[0,0],0)