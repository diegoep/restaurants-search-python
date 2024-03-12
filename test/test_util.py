import csv
import os
import pytest

from search.util import read_csv


@pytest.fixture
def sample_csv(tmpdir):
    # Create a sample CSV file for testing
    csv_data = [
        {'key': '1', 'value1': 'Apple', 'value2': 'Red'},
        {'key': '2', 'value1': 'Banana', 'value2': 'Yellow'},
        {'key': '3', 'value1': 'Orange', 'value2': 'Orange'},
    ]
    file_path = os.path.join(tmpdir, 'test_data.csv')

    with open(file_path, 'w', newline='') as file:
        headers = ['key', 'value1', 'value2']
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(csv_data)

    return file_path


def test_read_csv(sample_csv):
    # Test the read_csv function
    result = read_csv(sample_csv)

    assert len(result) == 3  # Check if three rows were read from the sample CSV

    # Check if keys 'key', 'value1', and 'value2' exist in the first row
    assert 'key' in result[0]
    assert 'value1' in result[0]
    assert 'value2' in result[0]

    # Check if values are read correctly for a specific row
    assert result[1]['key'] == '2'
    assert result[1]['value1'] == 'Banana'
    assert result[1]['value2'] == 'Yellow'
