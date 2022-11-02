from cipher_shh2145_2 import cipher_shh2145_2
import pytest

def test_cipher():
    example = 'friday'
    expected = 'gsjebz'
    actual = cipher_shh2145_2.cipher('friday', 1)
    assert actual == expected

test_cipher()