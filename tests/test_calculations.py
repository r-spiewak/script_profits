"""Tests for functions in calculations.py."""

from script_profits.calulations import (
    calculate_profits,
    convert_dollars_col,
    convert_dollars_elem,
)


def test_convert_dollars_elem(construct_test_series):
    """Tests convert_dollars_elem."""
    test_series, test_res = construct_test_series
    for val, res in zip(test_series, test_res):
        assert convert_dollars_elem(val) == res


def test_convert_dollars_col(construct_test_series):
    """Tests convert_dollars_col."""
    test_series, test_res = construct_test_series
    assert convert_dollars_col(test_series).equals(test_res)


def test_calculate_profits():
    """Tests calculate_profits."""
    assert (
        calculate_profits(
            {
                "verbosity": 0,
                "level": {
                    "basic": 1,
                    "extended": 2,
                },
            },
            "tests/test_db.csv",
            10,
            "profits",
        )
        == 1
    )
