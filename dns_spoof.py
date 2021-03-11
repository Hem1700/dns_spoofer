#!usr/bin/env/python

import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload()) # This will convert the packet payload to scapy packet
    print(scapy_packet)
    packet.drop()  # This will cut the connection of internet for the client
    #packet.accept() # This will accept the packet and forward it to the client computer allowing him to go that perticular website


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()