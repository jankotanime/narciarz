import pytest
import menu.ranking as ranking
import object.obstacles as obstacles


def test_score_search_1():
    assert (ranking.score_search(2000, 400, [2000, 800, 400], 900) == [2000, 900, 800, 400])


def test_death_function():
    assert (obstacles.death_function(200, 400, {'x1': 0, 'x2': 900, 'y1': 0, 'y2': 900}) == 1)


def test_ice_function():
    assert (obstacles.ice_function(900, 300, {'x1': 800, 'x2': 1200, 'y1': 900, 'y2': 1800}) is None)


def test_death_border_function():
    assert (obstacles.death_border_function(1200, 350, {'x1': 100, 'x2': 1100, 'y1': 0, 'y2': 900}) == 1)


def test_randomise_forest():
    assert (0 <= obstacles.randomise_forest() <= 4)
