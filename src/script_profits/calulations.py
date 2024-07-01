"""Functions to do the appropriate calculations."""

from pathlib import Path

import pandas


def convert_dollars_elem(elem: str) -> float:
    """Converts a str element into a numerical dollar."""
    return float(elem.replace("$", "").replace(",", ""))


def convert_dollars_col(col: pandas.Series) -> pandas.Series:
    """Converts a column of dollars to floats."""
    return col.apply(convert_dollars_elem)


def calculate_profits(
    state: dict,
    data: str,
    percentage: int,
    column: str,
) -> int:
    """Main calculation function.

    Args:
        state (dict): State dictionary, including keys
            such as verbosity.
        data (str): String representing path to data.
        percentage (int): Percentage of the top profits.
        column (str): Name of column in data containing
            the profits.

    Returns:
        int: Number of entries comprising the top
            percentage percent of the sum.
    """
    data_path = Path(data)
    data_table = pandas.read_csv(data_path)
    if state["verbosity"] > state["level"]["extended"]:
        print(f"data_table:\n{data_table}")
    # Need to convert from dollars?
    data_col = convert_dollars_col(data_table[column])
    summation = data_col.sum()
    if state["verbosity"] > state["level"]["basic"]:
        print(f"Sum: {summation}")
    sorted_values = data_col.sort_values(ascending=False)
    if state["verbosity"] > state["level"]["extended"]:
        print(f"sorted_values:\n{sorted_values}")
    dec = float(percentage) / float(100)
    count = 0
    running_talley = 0
    while running_talley < summation * dec:  # pylint: disable=while-used
        running_talley += sorted_values.iloc[count]
        if state["verbosity"] > state["level"]["basic"]:
            print(f"count {count}: talley {running_talley}")
        count += 1
    print(f"Number of entries in top {percentage} percent: {count}")
    return count
