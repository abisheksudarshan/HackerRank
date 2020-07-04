--Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.

Solution:

select distinct city from station where REGEXP_LIKE(city,'^[^AEIOU]')
