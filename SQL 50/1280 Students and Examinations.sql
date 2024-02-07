Select St.student_id, St.student_name, Su.subject_name, Count(e.student_id) AS attended_exams
From Students St Cross Join Subjects Su
Left Join Examinations as e
ON St.student_id = e.student_id And Su.subject_name = e.subject_name
Group by St.student_id, St.student_name, Su.subject_name
Order by St.student_id, Su.subject_name