--Query the smallest Northern Latitude (LAT_N) from STATION that is greater than 38.7880. Round your answer to 4 decimal places.

Solution:

select round(min(lat_n),4) from station where lat_N>38.7780;
