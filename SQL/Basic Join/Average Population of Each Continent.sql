/*Given the CITY and COUNTRY tables, query the names of all the continents (COUNTRY.Continent) and their respective average city populations (CITY.Population) rounded down to the nearest integer.

Note: CITY.CountryCode and COUNTRY.Code are matching key columns.*/

Solution:

select continent,floor(avg(b.population))
from country a
join city b
on a.code=b.countrycode
group by continent;
