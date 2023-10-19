-- Lists all records of second_table of the hbtn_0c_0 database

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
