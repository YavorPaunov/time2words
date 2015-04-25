import unittest

import time2words


class TestAproxTime(unittest.TestCase):

    def test_less_than_1m(self):
        self.assertEqual(
            time2words.approx_time(seconds=30), "thirty seconds")

        self.assertEqual(
            time2words.approx_time(seconds=24), "twenty-four seconds")

        self.assertEqual(
            time2words.approx_time(seconds=1), "one second")

        self.assertEqual(
            time2words.approx_time(seconds=11), "eleven seconds")

    def test_between_1m_and_1h(self):
        self.assertEqual(
            time2words.approx_time(minutes=1, seconds=30),
            "about one minute")

        self.assertEqual(
            time2words.approx_time(minutes=36, seconds=45),
            "about thirty-six minutes")

    def test_between_1h_and_23h(self):
        self.assertEqual(
            time2words.approx_time(hours=6, minutes=34),
            "six and a half hours")

        self.assertEqual(
            time2words.approx_time(hours=3, minutes=15),
            "more than three hours")

        self.assertEqual(
            time2words.approx_time(hours=7, minutes=54),
            "less than eight hours")

        self.assertEqual(
            time2words.approx_time(hours=13, minutes=57),
            "about fourteen hours")

    def test_between_23h_and_6d1h(self):
        self.assertEqual(
            time2words.approx_time(hours=23, minutes=30),
            "one day")

        self.assertEqual(
            time2words.approx_time(days=2, hours=13),
            "about two and a half days"
        )

        self.assertEqual(
            time2words.approx_time(days=4, hours=17),
            "a little less than five days"
        )

    def test_between_6d1h_and_25d10h(self):
        self.assertEqual(
            time2words.approx_time(days=11, hours=13),
            "about one and a half week"
        )

        self.assertEqual(
            time2words.approx_time(days=22, hours=11),
            "about three weeks"
        )

    def test_between_25d10h_and_11mm(self):
        self.assertEqual(
            time2words.approx_time(months=6, weeks=3, days=5),
            "about seven months"
        )

        self.assertEqual(
            time2words.approx_time(months=9, weeks=2),
            "about nine and a half months"
        )

    def test_between_11mm_and_11y(self):
        self.assertEqual(
            time2words.approx_time(months=11, days=5),
            "about one year"
        )

        self.assertEqual(
            time2words.approx_time(years=5, months=8, days=5),
            "less than six years"
        )

        self.assertEqual(
            time2words.approx_time(years=4, months=5),
            "about four and a half years"
        )

    def test_more_than_11y(self):
        self.assertEqual(
            time2words.approx_time(years=50, months=3),
            "about fifty years"
        )


if __name__ == '__main__':
    unittest.main()
