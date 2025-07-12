-- Script to create MySQL user user_0d_1 with all privileges
-- Create user with password (IF NOT EXISTS prevents failure if user already exists)
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grant all privileges to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
-- Flush privileges to ensure changes take effect
FLUSH PRIVILEGES;
