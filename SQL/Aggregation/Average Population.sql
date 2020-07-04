--Query the average population for all cities in CITY, rounded down to the nearest integer.

Solution:

select round(avg(population),0) from city ;
