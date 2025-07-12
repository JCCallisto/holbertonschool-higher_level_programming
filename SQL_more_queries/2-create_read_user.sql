-- Script to create database hbtn_0d_2 and user user_0d_2 with SELECT privileges
-- Create database (IF NOT EXISTS prevents failure if database already exists)
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create user with password (IF NOT EXISTS prevents failure if user already exists)
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grant SELECT privilege on the hbtn_0d_2 database to the user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
-- Flush privileges to ensure changes take effect
FLUSH PRIVILEGES;
