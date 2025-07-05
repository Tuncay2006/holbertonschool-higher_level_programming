-- Script to list all cities with their states, sorted by cities.id ascending
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
