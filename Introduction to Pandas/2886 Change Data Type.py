import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    convert ={
        'grade':int
    }
    students = students.astype(convert)
    return students