"""
There is a new mobile game that starts with consecutively numbered clouds.
Some of the clouds are thunderheads and others are cumulus. The player can
jump on any cumulus cloud having a number that is equal to the number of the
current cloud plus 1 or 2. The player must avoid the thunderheads.

Determine the minimum number of jumps it will take to jump from the starting
position to the last cloud. It is always possible to win the game.
"""

from enum import Enum

import pytest


class Cloud(Enum):
    CUMULUS = 0
    THUNDERHEAD = 1


def jumping_on_clouds(c: list[int]) -> int:
    index: int = 0
    jumps: int = 0

    while index != len(c) - 1:
        try:
            if c[index + 2] == Cloud.CUMULUS.value:
                index += 2
            else:
                index += 1
        except IndexError:
            index += 1

        jumps += 1

    return jumps


@pytest.mark.parametrize(
    "clouds, expected_jumps",
    [([0, 0, 1, 0, 0, 1, 0], 4), ([0, 0, 0, 0, 1, 0], 3), ([0, 0, 0, 0, 0, 0, 0], 3)],
)
def test_(clouds, expected_jumps):
    assert jumping_on_clouds(clouds) == expected_jumps
