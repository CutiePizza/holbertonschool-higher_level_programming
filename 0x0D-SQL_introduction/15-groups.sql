-- lists all the number of records with the same score
SELECT score, COUNT(score) AS number from second_table GROUP BY score;
