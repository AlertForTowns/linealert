from collections import defaultdict

def build_profile(packets):
    profile = {
        "detected_protocols": set(),
        "endpoint_summary": defaultdict(lambda: {"packet_count": 0}),
        "port_activity": defaultdict(lambda: {"TCP": set(), "UDP": set()}),
        "protocol_stats": defaultdict(lambda: {"packet_count": 0, "byte_count": 0}),
        "conversations": defaultdict(lambda: {"packet_count": 0})
    }

    for pkt in packets:
        try:
            if hasattr(pkt, "IP"):
                ip_layer = pkt["IP"]
                src_ip = ip_layer.src
                dst_ip = ip_layer.dst
            else:
                continue

            proto = None
            src_port = dst_port = 0

            if hasattr(pkt, "TCP"):
                tcp_layer = pkt["TCP"]
                src_port = tcp_layer.sport
                dst_port = tcp_layer.dport
                proto = "TCP"
            elif hasattr(pkt, "UDP"):
                udp_layer = pkt["UDP"]
                src_port = udp_layer.sport
                dst_port = udp_layer.dport
                proto = "UDP"
            elif hasattr(pkt, "ICMP"):
                proto = "ICMP"

            if proto:
                profile["detected_protocols"].add(proto)
                profile["endpoint_summary"][src_ip]["packet_count"] += 1
                profile["protocol_stats"][proto]["packet_count"] += 1
                profile["protocol_stats"][proto]["byte_count"] += len(pkt)

                if proto in ["TCP", "UDP"]:
                    profile["port_activity"][src_ip][proto].add(src_port)
                    profile["port_activity"][dst_ip][proto].add(dst_port)

                conv_key = f"{src_ip}:{src_port} -> {dst_ip}:{dst_port} ({proto})"
                profile["conversations"][conv_key]["packet_count"] += 1

        except Exception as e:
            print(f"[!] Skipping malformed packet: {e}")
            continue

    # Convert sets to lists for JSON serialization
    profile["detected_protocols"] = list(profile["detected_protocols"])
    for ip in profile["port_activity"]:
        profile["port_activity"][ip]["TCP"] = list(profile["port_activity"][ip]["TCP"])
        profile["port_activity"][ip]["UDP"] = list(profile["port_activity"][ip]["UDP"])

    return profile
