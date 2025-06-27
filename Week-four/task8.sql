SELECT H.hacker_id, H.name
FROM Hackers H
JOIN (
    SELECT S.hacker_id
    FROM Submissions S
    JOIN Challenges C ON S.challenge_id = C.challenge_id
    JOIN Difficulty D ON C.difficulty_level = D.difficulty_level
    WHERE S.score = D.score
    GROUP BY S.hacker_id, S.challenge_id
    HAVING COUNT(S.submission_id) > 0
) AS FullScoreHackers ON H.hacker_id = FullScoreHackers.hacker_id
GROUP BY H.hacker_id, H.name
HAVING COUNT(H.hacker_id) > 1
ORDER BY COUNT(H.hacker_id) DESC, H.hacker_id;