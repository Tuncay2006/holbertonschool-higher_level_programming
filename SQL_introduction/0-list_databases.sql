#!/bin/bash
-- Example comment required by validation tool
# Prompt for MySQL username
read -p "Enter MySQL username: " MYSQL_USER
# Prompt for MySQL password securely
read -s -p "Enter MySQL password: " MYSQL_PASS
echo
# List all databases
mysql -u "$MYSQL_USER" -p"$MYSQL_PASS" -e "SHOW DATABASES;"
