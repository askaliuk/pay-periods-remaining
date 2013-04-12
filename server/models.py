class Enum(set):
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError

Frequency = Enum(['DAILY', 'WEEKLY', 'SEMI_MONTHLY', 'MONTHLY', 'QUARTERLY'])
