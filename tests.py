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


# Data structure of the scores:
# [
#   {
#       "total": 3,
#       "score": (2, 1)
#   }
# ]

class KnownValues(unittest.TestCase):
    known_values = (
        [
            {
                "total": 5,
                "score": (1, 4)
            },
            {
                "total": 14,
                "score": (4, 5)
            },
            {
                "total": 29,
                "score": (6, 4)
            },
            {
                "total": 49,
                "score": (5, 5)
            },
            {
                "total": 60,
                "score": (10, 0)
            },
            {
                "total": 61,
                "score": (0, 1)
            },
            {
                "total": 77,
                "score": (7, 3)
            },
            {
                "total": 97,
                "score": (6, 4)
            },
            {
                "total": 117,
                "score": (10, 0)
            },
            {
                "total": 133,
                "score": (2, 8, 6)
            }
        ]
    )


if __name__ == "__main__":
    unittest.main()
