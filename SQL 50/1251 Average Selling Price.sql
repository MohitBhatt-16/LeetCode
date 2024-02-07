With my_cte as(
Select p.product_id, p.price, u.units 
from Prices p Left JOIN UnitsSold u on p.product_id = u.product_id and u.purchase_date Between start_date and end_date
)
Select product_id, IFNULL(ROUND(SUM(units*price)/SUM(units),2),0) as average_price 
From my_cte 
Group by product_id