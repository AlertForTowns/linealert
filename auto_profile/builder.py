import json
from scapy.all import rdpcap, TCP, UDP, IP


def build_profile(pcap_file):
    packets = rdpcap(pcap_file)
    profile = {
        "protocols_detected": {},
        "ports_observed": set()
    }

    for pkt in packets:
        if IP in pkt:
            proto = pkt[IP].proto
            if proto == 6 and TCP in pkt:
                protocol = "TCP"
                sport = pkt[TCP].sport
                dport = pkt[TCP].dport
            elif proto == 17 and UDP in pkt:
                protocol = "UDP"
                sport = pkt[UDP].sport
                dport = pkt[UDP].dport
            else:
                continue

            profile["protocols_detected"].setdefault(protocol, 0)
            profile["protocols_detected"][protocol] += 1
            profile["ports_observed"].update([sport, dport])

    # Convert set to list for JSON serialization
    profile["ports_observed"] = sorted(list(profile["ports_observed"]))

    return profile


def save_profile(profile, output_file):
    with open(output_file, 'w') as f:
        json.dump(profile, f, indent=4)
