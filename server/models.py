class Frequency(object):
    SEMI_MONTHLY = 'sm'

    @staticmethod
    def is_valid(frequency):
        return frequency in [Frequency.SEMI_MONTHLY]

