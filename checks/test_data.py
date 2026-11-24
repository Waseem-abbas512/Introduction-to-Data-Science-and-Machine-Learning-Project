import csv
from urllib.request import urlopen


SALES_DATA_URL = (
    "https://raw.githubusercontent.com/opencampus-sh/"
    "intro-to-data-science-and-ml/main/data/bakery/umsatzdaten_gekuerzt.csv"
)


def test_sales_dataset_can_be_loaded():
    with urlopen(SALES_DATA_URL, timeout=30) as response:
        rows = csv.reader(line.decode("utf-8-sig") for line in response)
        header = next(rows, None)
        first_row = next(rows, None)

    assert header
    assert first_row
    assert len(first_row) == len(header)
