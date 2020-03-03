-- list all shows
-- in hbtn_0d_tvshows
SELECT tv_shows.title AS title, tv_show_genres.genre_id AS genre_id FROM tv_show_genres LEFT JOIN tv_shows ON tv_show_genres.show_id=tv_shows.id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC WHERE tv_show_genres.show_id IS NULL OR tv_shows.id IS NULL;
