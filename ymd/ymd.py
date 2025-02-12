import datetime
import zoneinfo
from typing import List, Iterator


def date_range(
    start: str | datetime.date | datetime.datetime | int,
    stop: str | datetime.date | datetime.datetime | int,
    step: int = 1,
    format: str = "%Y-%m-%d",
    timezone: str = None
) -> Iterator[str]:
    """
    Return an object that produces a sequence of date strings from
    start (inclusive) to stop (exclusive) by step. When step is given,
    it specifies the increment (or decrement) in days.
    """
    if isinstance(start, int):
        start = today(offset=start, timezone=timezone)
    else:
        date = datetime.date(*tuple(map(int, str(start)[:10].split("-"))))
    if isinstance(stop, int):
        stop = date + datetime.timedelta(days=stop)
    else:
        stop = datetime.date(*tuple(map(int, str(stop)[:10].split("-"))))
    while True:
        if (date >= stop and step > 0) or (date <= stop and step < 0):
            break
        yield date.strftime(format)
        date = date + datetime.timedelta(days=step)
    return None


def date_list(
    start: str | datetime.date,
    stop: str | datetime.date | int,
    step: int = 1,
    format: str = "%Y-%m-%d",
) -> List[str]:
    """
    Return a list of date strings from start (inclusive) to stop (exclusive)
    by step. When step is given, it specifies the increment (or decrement).
    """
    return list(date_range(start, stop, step, format))


def today(offset: int = 0, timezone: str = None, format: str = "%Y-%m-%d"):
    """
    Return current date with an optional offset in days.
    """
    if timezone:
        date = datetime.datetime.now(tz=zoneinfo.ZoneInfo(timezone))
    else:
        date = datetime.date.today()
    if offset:
        date = date + datetime.timedelta(days=offset)
    return date.strftime(format)
