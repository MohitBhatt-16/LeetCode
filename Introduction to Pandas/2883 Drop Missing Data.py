
import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students.dropna(subset = ['name'],inplace = True, axis = 0)
    return students