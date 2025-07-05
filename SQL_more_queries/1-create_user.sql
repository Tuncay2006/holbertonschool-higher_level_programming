-- Script to create user_0d_1 with full privileges
-- 1. Create the user if not exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- 2. Grant all privileges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
-- 3. Apply the changes
FLUSH PRIVILEGES;
