import random

import pytest


def sock_merchant(_: int, ar: list[int]) -> int:
    socks: dict[int, int] = {}

    for sock in ar:
        socks[sock] = socks[sock] + 1 if socks.get(sock, None) else 1

    return sum(s // 2 for s in socks.values())


@pytest.mark.parametrize(
    "socks, expected_pairs",
    [
        ([], 0),
        ([[10, 10, 20, 30], 1]),
        ([[10, 10, 10, 10, 20, 30], 2]),
        ([10, 20, 20, 10, 10, 30, 50], 2),
        ([10, 20, 20, 10, 10, 30, 50, 10, 20], 3),
        ([10, 20, 20, 10, 10, 30, 50, 10, 20, 20, 10], 4),
    ],
)
def test_sock_merchant(socks, expected_pairs):
    assert sock_merchant(random.randint(1, 101), socks) == expected_pairs
