-- Script that lists all genres and displays the number of shows linked to each
-- Don't display genres that don't have any shows linked
-- Results sorted in descending order by the number of shows linked

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
