Select employee_id, department_id
From Employee
Where primary_flag = 'Y'
UNION
Select employee_id, department_id
From Employee
Group by employee_id
Having Count(department_id) = 1