-- Script that lists all genres of the show 'Dexter'
-- Uses JOINs to connect tv_shows, tv_show_genres, and tv_genres tables
-- Results sorted in ascending order by genre name

SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
