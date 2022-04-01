import pytest
from viewing_party.movie import Movie

def test_new_valid_movie():
    # Arrange
    title = "Star Wars"
    genre = "Sci-Fi"
    rating = 5
    host = "Netflix"

    # Act

    star_wars = Movie(title=title, genre=genre, rating=rating, host=host)

    # Assert

    assert star_wars.title == title
    assert star_wars.genre == genre
    assert star_wars.rating == rating
    assert star_wars.host == host

def test_update_movie_rating():
    # Arrange
    star_wars = Movie(title="Star Wars", genre="Sci-fi", rating=5, host = "Netflix")
    # Act
    star_wars.update_rating(4)
    # Assert
    assert star_wars.rating == 4
