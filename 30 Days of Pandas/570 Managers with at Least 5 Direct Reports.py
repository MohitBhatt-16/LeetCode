import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    op = pd.DataFrame(columns = ['name'])
    df = employee.groupby('managerId').count().reset_index()
    for index, row in df.iterrows():
        if row['id']>=5:
            for i , r in employee.iterrows():
                if r['id'] ==row['managerId']:
                    op = op._append({'name':r['name']},ignore_index = True)

    return op