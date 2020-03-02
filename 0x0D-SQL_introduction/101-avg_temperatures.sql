-- script that displays the average temperatures
SELECT city, AVG(value) as avg_tmp FROM temperatures GROUP BY city ORDER BY AVG(value) DESC;
