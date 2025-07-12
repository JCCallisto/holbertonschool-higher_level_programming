-- Script to create table id_not_null
-- Create table (IF NOT EXISTS prevents failure if table already exists)
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
