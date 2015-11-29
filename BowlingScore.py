

# Define exceptions
class BowlingError(Exception):
    pass


class NegativePinError(BowlingError):
    pass


class NotIntegerPinError(BowlingError):
    pass


class TooBigPinError(BowlingError):
    pass


class WrongTriesInFrame(BowlingError):
    pass


class TooManyFramesError(BowlingError):
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

    @property
    def score(self):
        return self._score

    def get_totals(self):
        return [x["total"] for x in self.score]

    def get_pins(self):
        return [x["pins"] for x in self.score]

    def add_pins(self, *args):
        '''
        Add tuple of pin scores.
        '''

        if len(self.score) >= 10:
            raise TooManyFramesError

        # Check all the pin elements are integers.
        if not all(isinstance(x, int) for x in args):
            raise NotIntegerPinError
        # That they are non negative.
        if not all(x >= 0 for x in args):
            raise NegativePinError

        # For the number of frames less than or equal to 9, check the number of
        # tries is less than 2, and no more than 10 pins are knocked down
        if len(self._score) < 9:
            if not len(args) == 2:
                raise WrongTriesInFrame
            if sum(args) > 10:
                raise TooBigPinError

            # Total is None to indicate it needs calculating
            self._score.append({"pins": args, "total": None})

        # Last fetch has slightly different rules
        elif len(self._score) == 9:
            if not len(args) == 2 or len(args) == 3:
                raise WrongTriesInFrame
            if sum(args) > 30:
                raise TooBigPinError

            self._score.append({"pins": args, "total": None})

    def calculate_total(self):
        pass
