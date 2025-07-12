-- Script to create table force_name
-- Create table (IF NOT EXISTS prevents failure if table already exists)
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
