import seconds2dd as sec

import pytest

def test_ddhhmmss():
    # 27000 == 1 x 7.5h day
    # 86400 == 1 x 24h day
    assert sec.ddhhmmss(0) == '00:00:00:00'
    assert sec.ddhhmmss(2) == '00:00:00:02'
    assert sec.ddhhmmss(12 * 60) == '00:00:12:00'
    assert sec.ddhhmmss(3600) == '00:01:00:00'
    assert sec.ddhhmmss(10 * 27000) == '10:00:00:00'
    assert sec.ddhhmmss(27000 + 5 * 3600 + 30 * 60 + 1) == '01:05:30:01'
    assert sec.ddhhmmss(365 * 27000) == '365:00:00:00'