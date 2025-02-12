import ymd


def test_date_list():
    assert ymd.date_list("2025-01-01", "2025-01-05") == [
        "2025-01-01",
        "2025-01-02",
        "2025-01-03",
        "2025-01-04",
    ]
    assert ymd.date_list("2025-01-01", 4) == [
        "2025-01-01",
        "2025-01-02",
        "2025-01-03",
        "2025-01-04",
    ]
    assert ymd.date_list("2025-01-05", "2025-01-01", -1) == [
        "2025-01-05",
        "2025-01-04",
        "2025-01-03",
        "2025-01-02",
    ]
    assert ymd.date_list("2025-01-01", 5, 2) == [
        "2025-01-01",
        "2025-01-03",
        "2025-01-05"
    ]
    assert ymd.date_list("2025-01-01", 6, 2) == [
        "2025-01-01",
        "2025-01-03",
        "2025-01-05"
    ]
    assert ymd.date_list("2025-01-10", -3, -1) == [
        "2025-01-10",
        "2025-01-09",
        "2025-01-08"
    ]


def test_today():
    today = ymd.today()
    tomorrow = ymd.today(offset=1)
    yesterday = ymd.today(offset=-1)
    assert ymd.date_list(0, 2) == [today, tomorrow]
    assert ymd.date_list(0, -2, -1) == [today, yesterday]
    assert ymd.date_list(0, 0) == []
    assert ymd.date_list(0, -1, -1) == [today]
