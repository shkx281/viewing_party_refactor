import pytest
from viewing_party.person import Person

def test_new_valid_person():
    # Arrange
    name = "Bob"
    watched = ["Star Wars", "Spongebob"]
    friends = ["Mandy", "Nish"]
    subscriptions = ["Hulu", "DisneyPlus", "HBOMax", "Netflix"]
    # Act

    bob = Person(name=name, watched=watched, friends=friends, subscriptions=subscriptions)

    # Assert

    assert bob.name == name
    assert bob.watched == watched
    assert bob.friends == friends
    assert bob.subscriptions == subscriptions

def test_add_watched_movie():
    # Arrange
    name = "Bob"
    watched = ["Star Wars", "Spongebob"]
    friends = ["Mandy", "Nish"]
    subscriptions = ["Hulu", "DisneyPlus", "HBOMax", "Netflix"]

    bob = Person(name=name, watched=watched, friends=friends, subscriptions=subscriptions)

    # Act
    bob.add_watched_movie("Shrek")

    # Assert
    assert bob.watched == ["Star Wars", "Spongebob", "Shrek"]

def test_num_of_movies_watched():
    # Arrange
    name = "Bob"
    watched = ["Star Wars", "Spongebob"]
    friends = ["Mandy", "Nish"]
    subscriptions = ["Hulu", "DisneyPlus", "HBOMax", "Netflix"]

    bob = Person(name=name, watched=watched, friends=friends, subscriptions=subscriptions)
    # Assert

    assert bob.get_num_watched() == 2

    
