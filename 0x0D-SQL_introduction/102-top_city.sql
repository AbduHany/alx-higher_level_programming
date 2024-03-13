-- This script  displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month = 8 OR month = 7
GROUP BY city
ORDER BY AVG(value) DESC
LIMIT 3;
