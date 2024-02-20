With my_cte as(
Select num
from MyNumbers 
group by num
having count(num) = 1
)

Select MAX(num) as num from my_cte