With my_cte as(
Select machine_id, process_id,
SUM( Case when activity_type = 'start' then -timestamp else timestamp end) as avg_timestamp
From Activity
group by machine_id,process_id)

Select machine_id, Round(AVG(avg_timestamp),3) as processing_time From my_cte
group by machine_id