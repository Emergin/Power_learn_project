-- undestanding Order by clause 
-- helps sort data retrieved by a select statement, it follows the where clause and specifies the column to sort by 
-- syntax
-- SELECT column1, column2, FROM table_name
-- where condition
-- ORDER BY column_name ASC|DESC;

-- Sorting by a single column
-- example 
SELECT * FROM records
ORDER BY date DESC;

-- sroting by multiple columns 
-- example 
SELECT * FROM records
ORDER BY category ASC, date DESC;

