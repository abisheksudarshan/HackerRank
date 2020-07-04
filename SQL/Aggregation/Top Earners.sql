/*We define an employee's total earnings to be their monthly salary x months worked, and the maximum total earnings to be the maximum total earnings for any employee in the Employee table. Write a query to find the maximum total earnings for all employees as well as the total number of employees who have maximum total earnings. Then print these values as space-separated integers.*/

Solution:

select total_sal,count(*) from (select e.*, (salary*months) as total_sal from employee e) w where (total_sal)=(select max(salary*months) from employee) 
group by total_sal;
