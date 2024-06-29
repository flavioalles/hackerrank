"""
Two strings are anagrams of each other if the letters of one string can be
rearranged to form the other string. Given a string, find the number of pairs
of substrings of the string that are anagrams of each other.
"""

import pytest


def hash_string(a_string: str) -> str:
    return "".join(sorted(a_string))


def sherlock_and_anagrams(the_string: str) -> int:
    occurrences: dict[str, int] = {}
    pairs: dict[str, int] = {}

    # For every length l within 1 through len(s) - 1
    # For every substring ss with length l
    # Is there another substring that is an anagram of it
    for length in range(1, len(the_string)):
        for index in range(len(the_string) - length + 1):
            substring = hash_string(the_string[index : index + length])
            try:
                occurrences[substring] += 1
            except KeyError:
                occurrences[substring] = 1

    # Determine number of pairs for each substring
    for substring in occurrences:
        pairs[substring] = (occurrences[substring] * (occurrences[substring] - 1)) // 2

    return sum(pairs.values())


@pytest.mark.parametrize(
    "the_string, expected_anagrams",
    [("abba", 4), ("abcd", 0), ("ifailuhkqq", 3), ("kkkk", 10), ("cdcd", 5)],
)
def test_sherlock_and_anagrams(the_string, expected_anagrams):
    assert sherlock_and_anagrams(the_string) == expected_anagrams
