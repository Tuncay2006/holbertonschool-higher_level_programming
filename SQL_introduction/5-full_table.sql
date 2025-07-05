-- prints the structure of first_table without using DESCRIBE or EXPLAIN
SELECT 
    COLUMN_NAME, 
    COLUMN_TYPE, 
    IS_NULLABLE, 
    COLUMN_DEFAULT 
FROM 
    information_schema.columns
WHERE 
    table_schema = DATABASE()
    AND table_name = 'first_table'
ORDER BY 
    ORDINAL_POSITION;
