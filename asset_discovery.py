import ipaddress
import subprocess

class AssetDiscovery:
    # Assuming the class already has other methods and initializations

    def ip_in_subnet(self, ip):
        """
        Check if an IP address is in a given subnet
        """
        try:
            ip_obj = ipaddress.ip_address(ip)
            subnet = ipaddress.ip_network('192.168.1.0/24', strict=False)  # Example subnet
            return ip_obj in subnet
        except ValueError as e:
            print(f"Invalid IP address: {ip}. Error: {e}")
            return False
