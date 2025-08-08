-- Advanced data retrieval 
-- wildcards [%] for flexible searching
-- they are your secret weapon for finding records with variations in wording 
-- example 
SELECT * FROM records
WHERE description LIKE '%keywords%';

-- This query retrieves all records where the description contains a "keyword" anywhere in the text. 
-- The % symbol acts as a wildcard, 
-- matching any characters before or after the "keyword." Perfect for capturing variations and synonyms!

-- comparison operators for targeted filtering 
-- example 
SELECT * FROM transactions
WHERE amount > 10000;

-- example 2 

SELECT * FROM events
WHERE event_date
BETWEEN '2025-12-21' AND '2026-01-01';

-- combining techniques for powerful queries 
-- example 3 
SELECT * FROM products
WHERE name
LIKE '%pro%' AND price >= 100;

