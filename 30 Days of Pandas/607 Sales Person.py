import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    op = pd.DataFrame(columns = ['name'])
    df = pd.merge(orders,company,on='com_id',how='inner')
    id = []
    for index, row in df.iterrows():
        if row['name'] == 'RED':
            id.append(row['sales_id'])
    for i, r in sales_person.iterrows():
        if r['sales_id'] not in id:
            op = op._append({'name' : r['name']},ignore_index = True)
    return op