import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether()
    broadcast =scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    print("IP\t\t\tMAC Address\n-----------------------------------------")
    clients_list = []
    
    for element in answered_list:
        client_dict = {"ip":element[1].psrc, "MAC":element[1].hwsrc}
        clients_list.append(client_dict)
        print(element[1].psrc + "\t\t" + element[1].hwsrc)
    print(clients_list)

scan('10.211.55.0/24')