SELECT
    h.hacker_id,
    h.name,
    SUM(max_score) AS total_score
FROM
    (
        SELECT
            hacker_id,
            challenge_id,
            MAX(score) AS max_score
        FROM
            submissions
        GROUP BY
            hacker_id,
            challenge_id
    ) AS sub
JOIN
    hackers h ON sub.hacker_id = h.hacker_id
GROUP BY
    h.hacker_id,
    h.name
HAVING
    SUM(max_score) > 0
ORDER BY
    total_score DESC,
    h.hacker_id;