-- a script that lists all shows contained in hbtn_0d_tvshows
SELECT t.title, tg.genre_id
FROM tv.shows INNER JOIN tv_show_genres
ORDER BY tv_shows.title = tv_show_genres.genre_id; 
