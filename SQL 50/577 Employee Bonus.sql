Select Employee.name,Bonus.bonus 
From Employee Left JOIN Bonus on Employee.empId = Bonus.empId
Where bonus<1000 OR bonus is Null