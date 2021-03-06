#!usr/bin/env/python

import netfilterqueue

def process_packet(packet):
    print(packet)
    packet.drop()  # This will cut the connection of internet for the client
    #packet.accept() # This will accept the packet and forward it to the client computer allowing him to go that perticular website


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()