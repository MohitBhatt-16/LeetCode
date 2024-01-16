import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    students = pd.merge(students, subjects, how = 'cross').sort_values(by=['student_id','subject_name'])
    examinations['attended_exams'] = 0
    examinations= examinations.groupby(['student_id','subject_name']).count().reset_index()
    merged_df = pd.merge(students, examinations, how = 'left',on = ['student_id','subject_name'])
    merged_df['attended_exams'] = merged_df['attended_exams'].fillna(0)
    return merged_df[['student_id','student_name','subject_name','attended_exams']]

    