SELECT W.id, WP.age, W.coins_needed, W.power
FROM Wands W
JOIN Wands_Property WP ON W.code = WP.code
WHERE WP.is_evil = 0 AND W.coins_needed = (
    SELECT MIN(coins_needed)
    FROM Wands
    JOIN Wands_Property ON Wands.code = Wands_Property.code
    WHERE Wands.power = W.power AND Wands_Property.age = WP.age
)
ORDER BY W.power DESC, WP.age DESC;
