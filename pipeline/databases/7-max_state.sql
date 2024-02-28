-- displays the MAX temperature (Fahrenheit)
--  of each state ordered by state name (descending)
SELECT state, MAX(value) AS max_temp FROM temperatures
GROUP BY state
ORDER BY max_temp DESC;
