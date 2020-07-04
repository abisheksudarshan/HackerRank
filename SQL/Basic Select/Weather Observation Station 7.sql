--Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.

Solution:

select distinct city from station where REGEXP_LIKE (city, '(*)[aeiou]$')
