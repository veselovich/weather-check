import pytest
from datetime import timedelta, datetime
from project import check_location, check_units, get_location, Forecast


def test_check_location():
    assert check_location("New York") is None
    assert check_location("Los Angeles, California") is None
    assert check_location("San Francisco, CA, USA") is None
    with pytest.raises(SystemExit):
        check_location("123 Invalid City")
    with pytest.raises(SystemExit):
        check_location("Miami, 123 Invalid State")
    with pytest.raises(SystemExit):
        check_location("")
    with pytest.raises(SystemExit):
        check_location("Chicago,, Illinois")


def test_check_units():
    assert check_units("metric") == None
    assert check_units("imperial") == None
    with pytest.raises(SystemExit):
        assert check_units("absolute")


def test_get_location():
    assert get_location("1.1.1.1") == ['Los Angeles,', 'California,', 'US']
    assert get_location("8.8.8.8") == ['Mountain View,', 'California,', 'US']
    with pytest.raises(SystemExit):
        assert get_location("275.3.6.28")


def test_is_tomorrow():
    instance = Forecast("")
    d1 = {"dt_txt": str((datetime.today() + timedelta(days=1)))}
    assert instance.is_tomorrow(d1) is True

    d2 = {"dt_txt": str(datetime.today())}
    assert instance.is_tomorrow(d2) is False
