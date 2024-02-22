Select E1.employee_id, E1.name, COUNT(E2.reports_to) as reports_count, Round(AVG(E2.age)) as average_age
from Employees E1 inner join Employees E2
on E1.employee_id = E2.reports_to
group by E2.reports_to
order by E1.employee_id
