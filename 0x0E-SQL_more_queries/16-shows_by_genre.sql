-- Write a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id 
GROUP BY genre ORDER BY number_of_shows DESC;
