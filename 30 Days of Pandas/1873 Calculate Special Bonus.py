import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    op = pd.DataFrame(columns = ['employee_id','bonus'])
    for index, row in employees.iterrows():
        if row['employee_id']%2 ==0 or row['name'].startswith("M"):
            op = op._append({'employee_id':row['employee_id'],
            'bonus': 0 }, ignore_index = True)
            
        else :
            op = op._append({'employee_id':row['employee_id'],
            'bonus':row['salary']}, ignore_index = True)
    op.sort_values(by='employee_id', inplace = True)   

    return op
    