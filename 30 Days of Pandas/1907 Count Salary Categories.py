import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    LowSalary = 0
    AverageSalary = 0
    HighSalary = 0
    for i in accounts['income']:
        if i < 20000:
            LowSalary = LowSalary + 1
        elif i >= 20000 and i <= 50000:
            AverageSalary = AverageSalary + 1
        elif i>50000:
            HighSalary = HighSalary + 1
    
    op = pd.DataFrame({'category': ['Low Salary','Average Salary','High Salary'],'accounts_count': [LowSalary,AverageSalary,HighSalary]})
    return op
    