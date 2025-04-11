import os
from auto_profile.snapshot_limiter import write_lasnap
from scapy.all import rdpcap
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def build_profile(packets):
    """Analyze the packets and build the protocol profile."""
    profile = {
        "detected_protocols": [],
        "endpoint_summary": {},
        "port_activity": {},
        "protocol_stats": {}
    }

    for pkt in packets:
        if hasattr(pkt, "ip"):
            ip_src = pkt["IP"].src
            ip_dst = pkt["IP"].dst
            proto = pkt["IP"].proto

            # Add protocol if not already in the list
            if proto == 6 and "TCP" not in profile["detected_protocols"]:
                profile["detected_protocols"].append("TCP")
            elif proto == 1 and "ICMP" not in profile["detected_protocols"]:
                profile["detected_protocols"].append("ICMP")

            # Increment packet count for each endpoint
            profile["endpoint_summary"][ip_src] = profile["endpoint_summary"].get(ip_src, {"packet_count": 0})
            profile["endpoint_summary"][ip_src]["packet_count"] += 1
            profile["endpoint_summary"][ip_dst] = profile["endpoint_summary"].get(ip_dst, {"packet_count": 0})
            profile["endpoint_summary"][ip_dst]["packet_count"] += 1

            # Track port activity
            if proto == 6:  # TCP
                src_port = pkt["TCP"].sport
                dst_port = pkt["TCP"].dport
                if ip_src not in profile["port_activity"]:
                    profile["port_activity"][ip_src] = {"TCP": [], "UDP": []}
                if ip_dst not in profile["port_activity"]:
                    profile["port_activity"][ip_dst] = {"TCP": [], "UDP": []}
                if src_port not in profile["port_activity"][ip_src]["TCP"]:
                    profile["port_activity"][ip_src]["TCP"].append(src_port)
                if dst_port not in profile["port_activity"][ip_dst]["TCP"]:
                    profile["port_activity"][ip_dst]["TCP"].append(dst_port)

    return profile

def main():
    pcap_path = "sample.pcap"  # Replace with your PCAP file path
    output_file = "new_profile.json"  # Output file for the profile
    
    # Read PCAP file and build profile
    packets = rdpcap(pcap_path)
    profile_data = build_profile(packets)

    # Write profile data to file
    write_lasnap(profile_data, "/home/azureuser/linealert/auto_profile/snapshots/snapshot_20250410T193803Z.lasnap")

if __name__ == "__main__":
    main()
