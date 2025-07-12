-- Script to list all cities of California using subquery
-- Select cities where state_id matches the id of California state
SELECT id, name FROM cities 
WHERE state_id = (SELECT id FROM states WHERE name = 'California') 
ORDER BY id ASC;
