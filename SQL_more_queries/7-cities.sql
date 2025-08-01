-- Script to create database hbtn_0d_usa and table cities
-- Create database (IF NOT EXISTS prevents failure if database already exists)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use the database
USE hbtn_0d_usa;
-- Create table cities (IF NOT EXISTS prevents failure if table already exists)
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
