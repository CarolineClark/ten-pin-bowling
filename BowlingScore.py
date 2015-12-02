

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


class WrongNumberOfFrames(BowlingError):
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
        self._scores = []

    @property
    def scores(self):
        return self._scores

    def get_totals(self):
        return [x["total"] for x in self.scores]

    def get_pins(self):
        return [x["pins"] for x in self.scores]

    def add_all_frames(self, pins):
        '''
        Add all frames into the class.
        :param pins: list of tuples of pin scores
        :type pins: list
        '''
        for pin in pins:
            self.add_frame(pin)

    # This is with the attitude of adding one frame at a time
    def add_frame(self, pin_tuple):
        '''
        Add tuple of pin scores, one at a time.
        '''

        if len(self.scores) >= 10:
            raise TooManyFramesError
        if not all(isinstance(x, int) for x in pin_tuple):
            raise NotIntegerPinError
        if not all(x >= 0 for x in pin_tuple):
            raise NegativePinError

        # For the number of frames less than or equal to 9, check the number of
        # tries is less than 2, and no more than 10 pins are knocked down
        if len(self.scores) < 9:
            self._add_regular_fetch_score(pin_tuple)

        # Last fetch has slightly different rules
        elif len(self.scores) == 9:
            self._add_last_fetch_score(pin_tuple)

    def _add_regular_fetch_score(self, pin_scores):
        if not len(pin_scores) == 2:
            raise WrongTriesInFrame
        if sum(pin_scores) > 10:
            raise TooBigPinError

        # Total is None to indicate it needs calculating
        self.scores.append({"pins": pin_scores, "total": None})

    def _add_last_fetch_score(self, pin_scores):
        if not (len(pin_scores) == 2 or len(pin_scores) == 3):
            raise WrongTriesInFrame
        if sum(pin_scores) > 30:
            raise TooBigPinError

        self.scores.append({"pins": pin_scores, "total": None})

    # Assumes you have all the pin scores
    def calculate_all_totals(self):
        self._check_number_of_frames()

        prev_total = 0
        for i in range(9):
            pins = self._scores[i]["pins"]
            future_pins = self._scores[i + 1]["pins"]
            self._scores[i]["total"] = self._calculate_non_final_total(
                prev_total, pins, future_pins
            )
            prev_total = self._scores[i]["total"]

        pins = self._scores[-1]["pins"]
        self._scores[-1]["total"] = self._calculate_final_total(
            prev_total, pins
        )

    def _check_number_of_frames(self):
        if not len(self._scores) == 10:
            raise WrongNumberOfFrames

    # This is for non final totals
    def _calculate_non_final_total(self, prev_total, pin_score,
                                   future_pin_score):

        pin_total = sum(pin_score)

        if pin_total < 10:
            return prev_total + pin_total
        elif 10 in pin_score:
            return prev_total + pin_total + future_pin_score[0] + \
                future_pin_score[1]
        else:
            return prev_total + pin_total + future_pin_score[0]

    # Is this that simple?
    def _calculate_final_total(self, prev_total, pin_score):
        return prev_total + sum(pin_score)
