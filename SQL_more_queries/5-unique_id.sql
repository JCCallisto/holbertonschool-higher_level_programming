-- Script to create table unique_id
-- Create table (IF NOT EXISTS prevents failure if table already exists)
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
