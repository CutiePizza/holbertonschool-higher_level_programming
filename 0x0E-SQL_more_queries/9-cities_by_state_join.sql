-- Join
-- Cities
SELECT cities.id AS id, cities.name AS name, states.name AS name FROM states
INNER JOIN cities ON cities.state_id=states.id
ORDER BY cities.id ASC;
