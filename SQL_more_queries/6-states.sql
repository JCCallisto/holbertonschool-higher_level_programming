-- Script to create database hbtn_0d_usa and table states
-- Create database (IF NOT EXISTS prevents failure if database already exists)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use the database
USE hbtn_0d_usa;
-- Create table states (IF NOT EXISTS prevents failure if table already exists)
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
