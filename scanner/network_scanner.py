import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)

scan('10.211.55.0/24')