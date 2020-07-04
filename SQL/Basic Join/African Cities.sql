/*Given the CITY and COUNTRY tables, query the names of all cities where the CONTINENT is 'Africa'.

Note: CITY.CountryCode and COUNTRY.Code are matching key columns.*/

Solution:

select name from city 
where countrycode in (select code from country where continent='Africa');
