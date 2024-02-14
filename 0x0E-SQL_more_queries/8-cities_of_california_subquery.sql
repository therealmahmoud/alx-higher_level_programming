-- a script that lists all the cities of California that can be found in the database hbtn_0d_usa.
USE hbtn_0d_usa;
SELECT `name`, `id` FROM *;
WHERE `name` = `California`;
ORDER BY city.id ASC;
