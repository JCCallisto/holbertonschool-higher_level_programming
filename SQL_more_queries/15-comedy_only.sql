-- Script that lists all Comedy shows in the database
-- Uses JOINs to connect tv_shows, tv_show_genres, and tv_genres tables
-- Results sorted in ascending order by show title

SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
