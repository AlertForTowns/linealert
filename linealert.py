from scapy.all import sniff, TCP, Raw, IP
from datetime import datetime

def alert(msg, pkt):
    print(f"[ALERT] {datetime.now()} - {msg} - SRC: {pkt[IP].src}")

def process_packet(pkt):
    if TCP in pkt and pkt[TCP].dport == 502 and Raw in pkt:
        payload = pkt[Raw].load
        if len(payload) >= 8:
            function_code = payload[7]
            if function_code in [5, 6, 15, 16]:  # 5 = Write Single Coil, 6 = Write Single Register, 15/16 = multiple writes
                alert(f"Modbus WRITE detected (function code {function_code})", pkt)

print("LineAlert is watching port 502 traffic for write operations...")
sniff(filter="tcp port 502", prn=process_packet, store=0)
