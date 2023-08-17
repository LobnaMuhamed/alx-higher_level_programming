-- a script that lists all shows contained in hbtn_0d_tvshows
SELECT t.title, tg.genre_id
FROM tv.shows AS t INNER JOIN tv_show_genres AS tg
ORDER BY tv_shows.title AND tv_show_genres.genre_id; 
