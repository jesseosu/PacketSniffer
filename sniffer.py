from scapy.all import sniff, IP, TCP, DNS, DNSQR, Raw
import socket
import re
from datetime import datetime

# Regular expression to capture HTTP Host header
HOST_REGEX = re.compile(r"(?i)Host:\s*(.*)")
visited = set()
packet_count = 0
captured_data = []

# Resolve IP to hostname
def resolve_ip(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return None

# Packet sniffing callback function
def packet_callback(packet):
    global packet_count
    packet_count += 1
    ip_layer = packet.getlayer(IP)
    if not ip_layer:
        return

    proto = None
    domain = None
    dst_ip = ip_layer.dst
    resolved_host = None

    if packet.haslayer(DNS) and packet.haslayer(DNSQR):
        domain = packet[DNSQR].qname.decode().strip(".")
        proto = "DNS"
    elif packet.haslayer(TCP):
        tcp_layer = packet.getlayer(TCP)
        proto = "HTTPS" if tcp_layer.dport == 443 else "HTTP"
        if packet.haslayer(Raw):
            try:
                payload = packet[Raw].load.decode("utf-8", errors="ignore")
                host_match = HOST_REGEX.search(payload)
                if host_match:
                    domain = host_match.group(1).strip()
            except Exception:
                pass

    if not domain:
        resolved_host = resolve_ip(dst_ip)
        if resolved_host:
            domain = resolved_host
            proto = "Reverse DNS"

    if domain and domain not in visited:
        visited.add(domain)
        captured_data.append({
            'timestamp': datetime.now().strftime("[%H:%M:%S]"),
            'protocol': proto,
            'domain': domain,
            'ip': dst_ip
        })

def start_sniffing():
    """Starts sniffing packets."""
    sniff(filter="tcp", prn=packet_callback, store=0)
