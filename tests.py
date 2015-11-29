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
    known_values = (
        [
            {
                "total": 5,
                "pins": (1, 4)
            },
            {
                "total": 14,
                "pins": (4, 5)
            },
            {
                "total": 29,
                "pins": (6, 4)
            },
            {
                "total": 49,
                "pins": (5, 5)
            },
            {
                "total": 60,
                "pins": (10, 0)
            },
            {
                "total": 61,
                "pins": (0, 1)
            },
            {
                "total": 77,
                "pins": (7, 3)
            },
            {
                "total": 97,
                "pins": (6, 4)
            },
            {
                "total": 117,
                "pins": (10, 0)
            },
            {
                "total": 133,
                "pins": (2, 8, 6)
            }
        ]
    )


class BadPinValues(unittest.TestCase):

    def test_negative(self):
        score = BowlingScore()
        self.assertRaises(NegativePinError, score.add_pins, -1, 2)

    def test_fractional(self):
        score = BowlingScore()
        self.assertRaises(NotIntegerPinError, score.add_pins, 0.5, 2)

    def test_big_total(self):
        score = BowlingScore()
        self.assertRaises(TooBigPinError, score.add_pins, 7, 7)

    def test_too_many_tries(self):
        score = BowlingScore()
        self.assertRaises(WrongTriesInFrame, score.add_pins, 1, 1, 1)

    def test_too_few_tries(self):
        score = BowlingScore()
        self.assertRaises(WrongTriesInFrame, score.add_pins, 1)

    def test_too_many_fetches(self):
        score = BowlingScore()
        for i in range(10):
            score.add_pins(1, 1)
        self.assertRaises(TooManyFramesError, score.add_pins, 1, 1)


if __name__ == "__main__":
    unittest.main()
