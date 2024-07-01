# Script Profits

Script to calculate the number of entries that make up the top `percentage` of `profits` in the appropriately named column of the `csv` file given in `data`.

## Installation

1. (If poetry is not already installed:) `curl -sSL https://install.python-poetry.org | python3 -`
2. `git clone https://github.com/r-spiewak/script_profits.git`
3. `poetry install`

## Dev Installation

After completing the regular installation above, also do the following:
1. `poetry run pre-commit install`

## Usage

`script_profits -d data [-p percentage] [-c column] [-vvvv]`
