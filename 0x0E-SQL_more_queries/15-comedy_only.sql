-- Ascript that lists all Comedy shows in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT
s.title

FROM
tv_genres AS g

JOIN
tv_show_genres AS sg

ON
g.id = sg.genre_id

JOIN
tv_shows AS s

ON
sg.show_id = s.id

WHERE
g.name = 'comedy'

ORDER BY
s.title ASC;
