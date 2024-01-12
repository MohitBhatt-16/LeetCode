import pandas as pd
import re

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    op = pd.DataFrame(columns=['patient_id','patient_name','conditions'])
    for index, row in patients.iterrows():
        if bool(re.search(r'^DIAB1|\sDIAB1',row['conditions'])):
            op = op._append({'patient_id':row['patient_id'],'patient_name':row['patient_name'],'conditions':row['conditions']}, ignore_index = True)   
    op.sort_values(by='patient_id',inplace = True)
    return op     
    