Select s.user_id, Round(Avg(if(c.action = 'confirmed',1,0)), 2) as confirmation_rate 
From Signups as s Left Join Confirmations as c on s.user_id = c.user_id 
group by s.user_id
