from enum import Enum
from random import randint

import pytest


class Step(Enum):
    DOWN = "D"
    UP = "U"


def counting_valleys(_: int, path: str) -> int:
    """
    Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.
    """
    level: int = 0
    valley: bool = False
    valleys: int = 0

    for step in path:
        level += 1 if step == Step.UP.value else -1
        if level < 0 and valley is False:
            valley = True
        elif level == 0 and valley is True:
            valleys += 1
            valley = False

    return valleys


@pytest.mark.parametrize("path, expected_valleys", [("DDUUDDUDUUUD", 2)])
def test_counting_valleys(path, expected_valleys):
    assert counting_valleys(randint(1, 101), path) == expected_valleys
