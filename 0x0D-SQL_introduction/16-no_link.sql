-- lists all records of the table second_table
--  display the score and the name
-- records are listed by descending score
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
