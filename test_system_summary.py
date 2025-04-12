import pytest
from system_summary import get_system_summary

def test_get_system_summary():
    summary = get_system_summary()
    assert isinstance(summary, dict), "The result should be a dictionary"
    assert 'CPU Usage (%)' in summary, "The summary should contain CPU usage"
    assert 'Memory Usage (%)' in summary, "The summary should contain memory usage"
    assert 'Disk Usage (%)' in summary, "The summary should contain disk usage"
