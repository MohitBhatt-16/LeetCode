Select query_name, Round(AVG(rating/position),2) as quality , 
Round(100*sum(case when rating<3 then 1 else 0 end)/count(rating),2) as poor_query_percentage 
from Queries 
where query_name is not Null 
Group by query_name