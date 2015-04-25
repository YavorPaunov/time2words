from num2words import num2words
from utils import to_abs_seconds, is_within_interval, append_unit_suffix
from utils import normalize
from chain import Chain
from commands import LessThan1M, LessThan1H, LessThan23H, LessThan6D1H
from commands import LessThan25D10H, LessThan11MM, LessThan10Y, MoreThan10Y
from localization import locales, _default

__version__ = '0.0.2'


def approx_time(l10n=locales.get(_default), **kwargs):
    kwargs = normalize(**kwargs)

    cor = Chain()
    cor.add(LessThan1M(l10n, **kwargs))
    cor.add(LessThan1H(l10n, **kwargs))
    cor.add(LessThan23H(l10n, **kwargs))
    cor.add(LessThan6D1H(l10n, **kwargs))
    cor.add(LessThan25D10H(l10n, **kwargs))
    cor.add(LessThan11MM(l10n, **kwargs))
    cor.add(LessThan10Y(l10n, **kwargs))
    cor.add(MoreThan10Y(l10n, **kwargs))
    return cor.run()
