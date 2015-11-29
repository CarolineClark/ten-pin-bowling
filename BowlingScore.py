

# Define exceptions
class BowlingError(Exception):
    pass


class NegativePinError(BowlingError):
    pass


class NotIntegerPinError(BowlingError):
    pass


class TooBigPinError(BowlingError):
    pass


# Data structure of the scores:
# [
#   {
#       "total": 3,
#       "score": (2, 1)
#   }
# ]
class BowlingScore():
    def __init__(self):
        self._score = []

    def add_pins(self):
        '''
        Add tuple of pin scores.
        '''
        pass
