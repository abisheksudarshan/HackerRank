--Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates.

Solution:

select distinct city from station where REGEXP_INSTR(city,'[aeiou]$')<=0;
