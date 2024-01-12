import pandas as pd
import re

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    op = pd.DataFrame(columns =['user_id','name','mail'])
    for index, row in users.iterrows():
        if bool(re.match(r'^[a-zA-Z][a-zA-Z0-9._-]*@leetcode[.]com',row['mail'])):
            op = op._append({'user_id':row['user_id'],'name':row['name'],'mail':row['mail']},ignore_index = True)
    return op