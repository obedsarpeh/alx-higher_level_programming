-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download
-- copy text from download and create new file hbtn_0d_tvshows.sql,
-- paste copied text into file,
-- CREATE DATABASE IF NOT EXISTS hbtn_0d_tvshows;
-- IMPORT
-- mysql -hlocalhost -uroot -p hbtn_0d_tvshows < hbtn_0d_tvshows.sql
-- Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command 
SELECT
tv_shows.title,
tv_show_genres.genre_id

FROM
tv_shows

LEFT JOIN
tv_show_genres

ON
tv_shows.id = tv_show_genres.show_id

WHERE
tv_show_genres.show_id = NULL
ORDER BY
tv_shows.title ASC,
tv_show_genres.genre_id ASC;
