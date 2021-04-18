import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("diamonds", 1)
        self.card2 = Card("clubs", 9)
        self.card3 = Card("hearts", 2)
    


    def test_check_for_ace_true(self):
        result = CardGame.check_for_ace(self.card1)
        self.assertEqual(True, result)

    def test_check_for_ace_false(self):
        result = CardGame.check_for_ace(self.card2)
        self.assertEqual(False, result)

    
    def test_highest_card(self):
        result = CardGame.highest_card(self.card1, self.card2)
        self.assertEqual(self.card2, result)


    def test_cards_total(self):
        cards = [self.card1, self.card2, self.card3]
        result = CardGame.cards_total(cards)
        self.assertEqual("You have a total of 12", result)