import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    op = pd.DataFrame(columns = ['Department','Employee','Salary'])
    if employee.empty or department.empty:
        return op
    else :
        merge_df = employee.merge(department, left_on = 'departmentId', right_on = 'id', suffixes = ('_employee','_department'))
        highest_salary_df = merge_df.groupby('departmentId').apply(lambda x: x[x['salary']==x['salary'].max()])
        return highest_salary_df[['name_department','name_employee','salary']].rename(columns = {'name_department':'Department','name_employee':'Employee','salary':'Salary'})
    