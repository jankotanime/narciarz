import pytest
import menu.ranking as ranking


def test_score_search_1():
    assert (ranking.score_search(2000, 400, [2000, 800, 400], 900) ==
            [2000, 900, 800, 400])


def test_score_search_2():
    assert (ranking.score_search(2000, 400, [2000, 800, 700, 500, 400], 300) ==
            [2000, 800, 700, 500, 400])


def test_score_search_3():
    assert (ranking.score_search(600, 400, [600, 400], 900) ==
            [900, 600, 400])


def test_score_search_4():
    assert (ranking.score_search(20, 20, [20], 30) ==
            [30, 20])
    
    
def test_score_search_5():
    assert (ranking.score_search(2000, 400, [2000, 800, 400], 2100) ==
            [2100, 2000, 800, 400])


