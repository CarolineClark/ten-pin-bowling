

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
        if not all(isinstance(x, int) for x in args):
            raise NotIntegerPinError
        if not all(x >= 0 for x in args):
            raise NegativePinError

        # For the number of frames less than or equal to 9, check the number of
        # tries is less than 2, and no more than 10 pins are knocked down
        if len(self.score) < 9:
            self._add_regular_fetch_score(args)

        # Last fetch has slightly different rules
        elif len(self.score) == 9:
            self._add_last_fetch_score(args)

        self._calculate_last_total()

    def get_last_total(self):
        '''
        Return the last one with a total that isn't None
        '''

        for score in self.score[::-1]:
            if score["total"]:
                return score["total"]

    def _add_regular_fetch_score(self, pin_scores):
        if not len(pin_scores) == 2:
            raise WrongTriesInFrame
        if sum(pin_scores) > 10:
            raise TooBigPinError

        # Total is None to indicate it needs calculating
        self.score.append({"pins": pin_scores, "total": None})

    def _add_last_fetch_score(self, pin_scores):
        if not len(pin_scores) == 2 or len(pin_scores) == 3:
            raise WrongTriesInFrame
        if sum(pin_scores) > 30:
            raise TooBigPinError

        self.score.append({"pins": pin_scores, "total": None})

    def _calculate_last_total(self):
        # Take last section and check total:
        if self.score[-1]["total"] is None:

            if len(self.score) == 1:
                self.score[-1]["total"] = sum(self.score[-1]["pins"])
