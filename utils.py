# Импортируем модуль SQLite3 из стандартной библиотеки Python
import sqlite3


def get_movie_title(title):
    """
    Функция, которая возвращает фильм из БД по названию
    """
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"""
                   SELECT `title`, `country`, `release_year`, `listed_in`, `description` 
                   FROM netflix
                   WHERE title LIKE '%{title}%'
                   ORDER BY release_year DESC 
                       """
        )
        data = cursor.fetchone()
        movie = {
            "title": data[0],
            "country": data[1],
            "release_year": data[2],
            "genre": data[3],
            "description": data[4]
        }
        return movie


def get_by_years(year_1, year_2):
    """
    Функция, которая возвращает фильмы из БД по диапазону лет выпуска
    """
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"""
                   SELECT `title`, `release_year` 
                   FROM netflix
                   WHERE release_year BETWEEN {year_1} AND {year_2} 
                   LIMIT 100
                       """
        )
        data = cursor.fetchall()
        movies_list = []
        for i in data:
            movie = {
                "title": i[0],
                "release_year": i[1],
            }
            movies_list.append(movie)
        return movies_list


def get_rating_for_children():
    """
    Функция, которая возвращает фильмы из БД для детей
    """
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"""
                   SELECT `title`, `rating`, `description` 
                   FROM netflix
                   WHERE rating = 'G'
                   LIMIT 100
                       """
        )
        data = cursor.fetchall()
        movies_list = []
        for i in data:
            movie = {
                "title": i[0],
                "rating": i[1],
                "description": i[2]
            }
            movies_list.append(movie)
        return movies_list


def get_rating_for_family():
    """
    Функция, которая возвращает фильмы из БД для семейного просмотра
    """
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"""
                   SELECT `title`, `rating`, `description` 
                   FROM netflix
                   WHERE rating = 'G' OR rating = 'PG' OR rating = 'PG-13'
                   LIMIT 100
                       """
        )
        data = cursor.fetchall()
        movies_list = []
        for i in data:
            movie = {
                "title": i[0],
                "rating": i[1],
                "description": i[2]
            }
            movies_list.append(movie)
        return movies_list


def get_rating_for_adult():
    """
    Функция, которая возвращает фильмы из БД для взрослых
    """
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"""
                   SELECT `title`, `rating`, `description` 
                   FROM netflix
                   WHERE rating = 'R' OR rating = 'NC-17'
                   LIMIT 100
                       """
        )
        data = cursor.fetchall()
        movies_list = []
        for i in data:
            movie = {
                "title": i[0],
                "rating": i[1],
                "description": i[2]
            }
            movies_list.append(movie)
        return movies_list


def get_movie_by_genre(genre):
    """
    Функция, которая возвращает 10 новых фильмов из БД по жанру
    """
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"""
                   SELECT `title`, `description` 
                   FROM netflix
                   WHERE listed_in LIKE '%{genre}%'
                   ORDER BY release_year DESC 
                   LIMIT 10
                       """
        )
        data = cursor.fetchall()
        movies_list = []
        for i in data:
            movie = {
                "title": i[0],
                "description": i[1]
            }
            movies_list.append(movie)
        return movies_list


def get_by_cast(actor_1, actor_2):
    """
    Функция, которая возвращает список актёров, которые играют друг с другом больше 2 раз
    """
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"""
                   SELECT COUNT(netflix.cast), netflix.cast
                   FROM netflix
                   WHERE netflix.cast LIKE '%{actor_1}%' AND netflix.cast LIKE '%{actor_2}%'
                   GROUP BY netflix.cast
                   HAVING netflix.cast >= 2
                       """
        )
        data = cursor.fetchall()
        movies_list = []
        for i in data:
            movie = {
                "cast": i[1]
            }
            movies_list.append(movie)
        return movies_list


def get_find_a_movie(movie_type, release_year, genre):
    """
    Функция, которая возвращает список фильмов в зависимости от типа, года выпуска и жанра
    """
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"""
                   SELECT `title`, `description` 
                   FROM netflix
                   WHERE type LIKE '%{movie_type}%' AND release_year = {release_year} AND listed_in LIKE '%{genre}%'
                       """
        )
        data = cursor.fetchall()
        movies_list = []
        for i in data:
            movie = {
                "title": i[0],
                "description": i[1]
            }
            movies_list.append(movie)
        return movies_list
