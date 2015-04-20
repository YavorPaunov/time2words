from num2words import num2words
from utils import to_abs_seconds, is_within_interval, append_unit_suffix
from utils import normalize
from chain import Chain
from commands import LessThan1M, LessThan1H, LessThan23H, LessThan6D1H
from commands import LessThan25D10H, LessThan11MM, LessThan10Y, MoreThan10Y

__version__ = '0.0.1.dev01'


def approx_time(loc, **kwargs):
    kwargs = normalize(**kwargs)

    cor = Chain()
    cor.add(LessThan1M(loc, **kwargs))
    cor.add(LessThan1H(loc, **kwargs))
    cor.add(LessThan23H(loc, **kwargs))
    cor.add(LessThan6D1H(loc, **kwargs))
    cor.add(LessThan25D10H(loc, **kwargs))
    cor.add(LessThan11MM(loc, **kwargs))
    cor.add(LessThan10Y(loc, **kwargs))
    cor.add(MoreThan10Y(loc, **kwargs))
    return cor.run()
