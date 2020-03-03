-- SUbquery
-- Cities of California
SELECT id, name FROM cities where state_id = (
	SELECT id FROM states
	WHERE name = "California")
ORDER BY cities.id ASC;
