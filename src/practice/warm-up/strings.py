"""
There is a string, s, of lowercase English letters that is repeated infinitely many times.
Given an integer, n, find and print the number of letter a's in the first n letters of the
infinite string.
"""

import pytest


def repeated_string(s: str, n: int) -> int:
    substring = "a"
    return (s.count(substring) * (n // len(s))) + (s[: n % len(s)].count(substring))


@pytest.mark.parametrize(
    "s, n, expected_frequency",
    [
        ("aa", 10, 10),
        ("ab", 10, 5),
        ("aba", 10, 7),
        ("b", 10, 0),
        ("a", pow(10, 12), pow(10, 12)),
        ("b", pow(10, 12), 0),
        (
            "epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq",
            549382313570,
            16481469408,
        ),
    ],
)
def test_repeated_string(s, n, expected_frequency):
    assert repeated_string(s, n) == expected_frequency
