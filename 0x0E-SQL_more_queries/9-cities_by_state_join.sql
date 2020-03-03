-- Join
-- Cities
SELECT cities.id AS id, cities.name AS name, states.name AS name FROM cities
JOIN states ON cities.id=states.state_id
ORDER BY cities.id ASC;
