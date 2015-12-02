# Things to test:

# 1) If all the individual scores are less than 10:
#   i) the total score is the total
#   ii) the total number of frames is 10

# 2) If a score added is negative, should fail

# 3) If a score added is fractional, should fail

# 4) In frames 1-9, the number of balls should be 2.

# 5) In the last frame, the number of balls should be either 2 or 3

# 6) The max number of pins that can be knocked down in frames 1-9 is 10

# 7) The max number of pins that can be knocked down in frame 10 is 30.

# 8) The max total is 300

# 9) The min total is 0

# Individual scores
# 10) If 10 is knocked over within 2 tries
#   i) and they are within the same frame, check a bonus score is added
#   ii) if they are not in the same frame, check a bonus score is not added


import unittest
from BowlingScore import (
    BowlingScore, NegativePinError, NotIntegerPinError, TooBigPinError,
    WrongTriesInFrame, TooManyFramesError
)


class KnownValues(unittest.TestCase):

    known_values = {
        # No bonus
        "no-bonus": {
            "pins": [
                (1, 1),
                (1, 2),
                (2, 5),
                (3, 5),
                (7, 1),
                (4, 4),
                (5, 4),
                (9, 0),
                (0, 0),
                (0, 2)
            ],
            "totals": [2, 5, 12, 20, 28, 36, 45, 54, 54, 56]
        },
        # Basic bonus
        "basic-bonus": {
            "pins": [
                (1, 1),
                (1, 9),
                (2, 5),
                (3, 5),
                (7, 1),
                (4, 4),
                (5, 4),
                (9, 0),
                (0, 0),
                (0, 2)
            ],
            "totals": [2, 14, 21, 29, 37, 45, 54, 63, 63, 65]
        },
        # Strike
        "strike": {
            "pins": [
                (1, 1),
                (1, 2),
                (2, 5),
                (3, 5),
                (7, 1),
                (4, 4),
                (5, 4),
                (10, 0),
                (1, 0),
                (0, 2)
            ],
            "totals": [2, 5, 12, 20, 28, 36, 45, 56, 57, 59]
        },
        # Example from email
        "email-example": {
            "pins": [
                (1, 4),
                (4, 5),
                (6, 4),
                (5, 5),
                (10, 0),
                (0, 1),
                (7, 3),
                (6, 4),
                (10, 0),
                (2, 8, 6)
            ],
            "totals": [5, 14, 29, 49, 60, 61, 77, 97, 117, 133]
        }
    }

    def test_no_bonus(self):
        pins = self.known_values["no-bonus"]["pins"]
        totals = self.known_values["no-bonus"]["totals"]
        self.pins_vs_totals(pins, totals)

    def test_basic_bonus(self):
        pins = self.known_values["basic-bonus"]["pins"]
        totals = self.known_values["basic-bonus"]["totals"]
        self.pins_vs_totals(pins, totals)

    def test_strike(self):
        pins = self.known_values["strike"]["pins"]
        totals = self.known_values["strike"]["totals"]
        self.pins_vs_totals(pins, totals)

    def test_email_example(self):
        pins = self.known_values["email-example"]["pins"]
        totals = self.known_values["email-example"]["totals"]
        self.pins_vs_totals(pins, totals)

    def pins_vs_totals(self, pins, totals):
        score = BowlingScore()
        score.add_all_frames(pins)
        score.calculate_all_totals()
        self.assertEquals(score.get_totals(), totals)


class BadPinValues(unittest.TestCase):

    def test_negative(self):
        score = BowlingScore()
        self.assertRaises(NegativePinError, score.add_frame, (-1, 2))

    def test_fractional(self):
        score = BowlingScore()
        self.assertRaises(NotIntegerPinError, score.add_frame, (0.5, 2))

    def test_big_total(self):
        score = BowlingScore()
        self.assertRaises(TooBigPinError, score.add_frame, (7, 7))

    def test_too_many_tries(self):
        score = BowlingScore()
        self.assertRaises(WrongTriesInFrame, score.add_frame, (1, 1, 1))

    def test_too_few_tries(self):
        score = BowlingScore()
        self.assertRaises(WrongTriesInFrame, score.add_frame, (1,))

    def test_too_many_fetches(self):
        score = BowlingScore()
        for i in range(10):
            score.add_frame((1, 1))
        self.assertRaises(TooManyFramesError, score.add_frame, (1, 1))


if __name__ == "__main__":
    unittest.main()
