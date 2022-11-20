# Импортируем фреймворк Flask и его функции
from flask import Flask, jsonify

# Импортируем функции из utils.py, которые будем использовать
from utils import get_movie_title, get_by_years, get_rating_for_children, get_rating_for_family, get_rating_for_adult, \
    get_movie_by_genre, get_by_cast, get_find_a_movie

# Инициализируем приложение с конфигурационными файлами
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route("/movie/<title>")
def page_movie(title):
    """Страница с поиском по названию фильма"""
    movie = get_movie_title(title)
    return jsonify(movie)


@app.route("/movie/<int:year_1>/to/<int:year_2>")
def page_movies_by_years(year_1, year_2):
    """Страница с поиском по диапазону лет выпуска фильмов"""
    movies = get_by_years(year_1, year_2)
    return jsonify(movies)


@app.route("/rating/children")
def page_movies_for_children():
    """Страница с фильмами для детей"""
    movies = get_rating_for_children()
    return jsonify(movies)


@app.route("/rating/family")
def page_movies_for_family():
    """Страница с фильмами для семейного просмотра"""
    movies = get_rating_for_family()
    return jsonify(movies)


@app.route("/rating/adult")
def page_movies_for_adult():
    """Страница с фильмами для взрослых"""
    movies = get_rating_for_adult()
    return jsonify(movies)


@app.route("/genre/<genre>")
def page_movies_by_genre(genre):
    """Страница с поиском новых 10 фильмов по жанру"""
    movies = get_movie_by_genre(genre)
    return jsonify(movies)


@app.route("/cast/<actor_1>/<actor_2>")
def page_movie_cast(actor_1, actor_2):
    """Страница с поиском фильмов в которых актеры играют друг с другом больше 2 раз"""
    movies = get_by_cast(actor_1, actor_2)
    return jsonify(movies)


@app.route("/find/<movie_type>/<int:release_year>/<genre>")
def page_find_a_movie(movie_type, release_year, genre):
    """Страница с поиском фильмов в зависимости от типа, года выпуска и жанра"""
    movies = get_find_a_movie(movie_type, release_year, genre)
    return jsonify(movies)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
