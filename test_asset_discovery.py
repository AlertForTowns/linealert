import pytest
from asset_discovery import AssetDiscovery

def test_ip_in_subnet():
    asset_discovery = AssetDiscovery()
    
    # Test a valid IP within the subnet
    assert asset_discovery.ip_in_subnet('192.168.1.5') == True
    
    # Test a valid IP outside the subnet
    assert asset_discovery.ip_in_subnet('192.168.2.5') == False
    
    # Test an invalid IP
    assert asset_discovery.ip_in_subnet('invalid_ip') == False
