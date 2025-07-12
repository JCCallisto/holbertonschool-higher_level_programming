-- Script to list records from second_table excluding rows with no name value
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
