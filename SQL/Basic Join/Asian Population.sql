/*Given the CITY and COUNTRY tables, query the sum of the populations of all cities where the CONTINENT is 'Asia'.

Note: CITY.CountryCode and COUNTRY.Code are matching key columns.*/

Solution:

select sum(population) from city a
where countrycode in (select code from country where continent='Asia');
