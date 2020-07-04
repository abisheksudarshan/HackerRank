--Query a list of CITY names from STATION with even ID numbers only. You may print the results in any order, but must exclude duplicates from your answer.

Solution:

select city from station where id%2=0 group by 1
