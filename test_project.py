import pytest
from datetime import timedelta, datetime
from project import check_location, Forecast


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


def test_is_tomorrow():
    instance = Forecast("")
    d1 = {"dt_txt": str((datetime.today() + timedelta(days=1)))}
    assert instance.is_tomorrow(d1) is True

    d2 = {"dt_txt": str(datetime.today())}
    assert instance.is_tomorrow(d2) is False
