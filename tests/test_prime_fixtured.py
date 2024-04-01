import pytest

from prime.prime import is_prime


@pytest.fixture
def minus():
    return (-1, False)


def test_is_prime_minus(minus):
    number, expected = minus
    assert is_prime(number) == expected


@pytest.fixture
def prime_numbers():
    return [
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (6, False),
        (7, True),
        (8, False),
        (9, False),
        (10, False),
    ]


def test_is_prime(prime_numbers):
    for number, expected in prime_numbers:
        assert is_prime(number) == expected
