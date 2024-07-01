"""Fixtures for tests."""

import pandas
import pytest


@pytest.fixture
def construct_test_series():
    """Construct some Series for use in tests."""
    test_series = pandas.Series(
        [
            "$3.04",
            "-$3.40",
            "$1,001",
            "-$1,001.10",
        ]
    )
    test_res = pandas.Series(
        [
            3.04,
            -3.4,
            1001,
            -1001.1,
        ]
    )
    return test_series, test_res
