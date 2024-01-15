import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    op = pd.DataFrame(columns = ['class'])
    df = courses.groupby('class').count().reset_index()
    for index, row in df.iterrows():
        if row['student']>=5:
            op = op._append({'class':row['class']},ignore_index = True)
    return op

    