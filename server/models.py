class Frequency(object):
    data = ['SEMI_MONTHLY']

    def __getattr__(self, name):
        if name in Frequency.data:
            return name

    @staticmethod
    def is_valid(frequency):
        return frequency in Frequency.data
