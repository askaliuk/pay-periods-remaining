from datetime import datetime
from dateutil.rrule import rrule, MONTHLY


def pay_periods_remaining(start_date=None):
    if start_date is None:
        start_date = datetime.today()
    # TODO(askalyuk): semi-monthly support for now only
    rule = rrule(MONTHLY, until=datetime(2013, 12, 31),
                 dtstart=datetime(2013, 3, 18), bymonthday=[15, -1])
    return len(list(rule))
