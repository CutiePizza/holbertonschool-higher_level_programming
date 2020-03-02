-- Top three
SELECT city, AVG(value) as avg_tmp FROM temperatures WHERE month = 7 OR month = 8 GROUP BY city ORDER BY AVG(value) DESC LIMIT 3;