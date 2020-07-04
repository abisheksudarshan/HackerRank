--Query the greatest value of the Northern Latitudes (LAT_N) from STATION that is less than 137.2345. Truncate your answer to 4 decimal places.

Solution:

select round(max(lat_n),4) from station where lat_N<137.2345;
