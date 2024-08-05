-- A script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT
g.name,
SUM(sr.rate) AS rating

FROM
tv_genres AS g

JOIN
tv_show_genres AS sg

ON
g.id = sg.genre_id

JOIN
tv_show_ratings AS sr

ON
sr.show_id = sg.show_id

GROUP BY
g.name

ORDER BY
rating DESC;
