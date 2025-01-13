"""
CMSC 14200, Winter 2025
Homework #1, Task #4 (tests)

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

from task3 import Card
from task4 import are_compatible

def test_task4_compatible() -> None:
    """
    Write a test that creates three cards with these features:

    Card 1: {"color": "red", "shape": "circle", "number": "3"}
    Card 2: {"color": "red", "shape": "square", "number": "1"}
    Card 3: {"color": "red", "shape": "triangle", "number": "2"}
    Card 4: {"color": "red", "shape": "pentagon", "number": "4"}

    These cards are compatible, because there is only one common feature
    across all four cards ("color": "red").

    Your test must check that calling are_compatible with these cards
    returns the correct value.
    """
    card1 = Card({"color": "red", "shape": "circle", "number": "3"})
    card2 = Card({"color": "red", "shape": "square", "number": "1"})
    card3 = Card({"color": "red", "shape": "triangle", "number": "2"})
    card4 = Card({"color": "red", "shape": "pentagon", "number": "4"})
    actual = are_compatible([card1,card2,card3,card4])
    assert (actual is not None)
    assert (actual[0] == "color" or actual[1] == "red")
        


def test_task4_multiple_common_features() -> None:
    """
    Write a test with four cards that have *two* common features
    (and are thus not compatible). Check that are_compatible returns
    None for these cards.
    """
    card1 = Card({"color": "red", "shape": "circle", "number": "3"})
    card2 = Card({"color": "red", "shape": "circle", "number": "1"})
    card3 = Card({"color": "red", "shape": "circle", "number": "2"})
    card4 = Card({"color": "red", "shape": "circle", "number": "4"})
    actual = are_compatible([card1,card2,card3,card4])
    assert (actual is None)

def test_task4_single_card() -> None:
    """
    Write a test with a single card, and check that are_compatible
    returns None for this card.
    """
    card1 = Card({"color": "red", "shape": "circle", "number": "3"})
    actual = are_compatible([card1])
    assert (actual is None)

def test_task4_pairwise_compatible() -> None:
    """
    Write a test with three cards (A, B, and C) where:

    - A is compatible with B
    - A is compatible with C
    - B is compatible with C

    But all *three* cards are not compatible.

    Check that are_compatible returns the correct common feature when called
    on A and B, A and C, and B and C, but returns None when called on A, B,
    and C.
    """
    cardA = Card({"color": "red", "shape": "circle", "number": "3"})
    cardB = Card({"color": "red", "shape": "square", "number": "2"})
    cardC = Card({"color": "blue", "shape": "circle", "number": "2"})
    ABactual = are_compatible([cardA,cardB])
    ACactual = are_compatible([cardA,cardC])
    BCactual = are_compatible([cardB,cardC])
    allactual = are_compatible([cardA,cardB,cardC])
    assert ABactual == ("color","red")
    assert ACactual == ("shape","circle")
    assert BCactual == ("number","2")
    assert allactual is None