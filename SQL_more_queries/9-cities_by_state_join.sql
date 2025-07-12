-- Script to list all cities with their states using JOIN
-- Select cities.id, cities.name, and states.name joined by state_id
SELECT cities.id, cities.name, states.name 
FROM cities 
JOIN states ON cities.state_id = states.id 
ORDER BY cities.id ASC;
