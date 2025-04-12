# test_data_processing.py

from data_processing import process_data

def test_process_data():
    input_data = [1, 2, 3, 4]
    expected_output = [1, 4, 9, 16]
    assert process_data(input_data) == expected_output