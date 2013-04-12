from datetime import datetime
from dateutil.rrule import rrule, MONTHLY


def pay_periods_remaining(start_date):
    # TODO(askalyuk): semi-monthly support for now only
    # TODO(askalyuk): add doc string
    rule = rrule(MONTHLY, until=datetime(start_date.year, 12, 31),
                 dtstart=start_date, bymonthday=[15, -1])
    return len(list(rule))
