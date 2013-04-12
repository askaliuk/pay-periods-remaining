from datetime import datetime
from dateutil.rrule import rrule, MONTHLY, DAILY, WEEKLY, FR
from models import Frequency


# TODO(askalyuk): implement support payments in business days only
# TODO(askalyuk): implement bi-weekly support
def pay_periods_remaining(start_date, frequency):
    """Calculate the pay periods remaining from start date to the end of year.

    Args:
        start_date: the date to start calculation from.
        frequency: payment frequency (models.Frequency instance)
    Returns:
        the integer count of pay periods remaining.
    """
    if frequency == Frequency.DAILY:
        rule = rrule(DAILY, until=datetime(start_date.year, 12, 31),
                     dtstart=start_date)
    elif frequency == Frequency.WEEKLY:
        # pay each Friday
        rule = rrule(WEEKLY, until=datetime(start_date.year, 12, 31),
                     dtstart=start_date, byweekday=[FR])
    elif frequency == Frequency.SEMI_MONTHLY:
        # pay on 15th and last day of each month
        rule = rrule(MONTHLY, until=datetime(start_date.year, 12, 31),
                     dtstart=start_date, bymonthday=[15, -1])
    elif frequency == Frequency.MONTHLY:
        # pay on last day of each month
        rule = rrule(MONTHLY, until=datetime(start_date.year, 12, 31),
                     dtstart=start_date, bymonthday=[-1])
    elif frequency == Frequency.QUARTERLY:
        # pay on last day of each quarter
        rule = rrule(MONTHLY, bymonth=(3, 6, 9, 12),
                     bymonthday=[-1],
                     dtstart=start_date,
                     until=datetime(start_date.year, 12, 31))
    else:
        raise NotImplementedError
    return len(list(rule))
