--Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.

Solution:

select distinct city from station where id in (select distinct id from station where city REGEXP '^[^aeiou]' or city REGEXP '[^aeiou]$'); 
