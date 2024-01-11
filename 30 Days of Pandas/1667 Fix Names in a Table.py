import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    op = pd.DataFrame(columns= ['user_id','name'])
    for index, row in users.iterrows():
        n = row['name'][0].upper() + row['name'][1:].lower()
        op = op._append({'user_id':row['user_id'],'name':n}, ignore_index = True)
    op.sort_values(by='user_id',inplace = True)
    return op
