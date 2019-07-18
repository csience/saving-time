#!/usr/bin/env python2

import socket

target_host = "127.0.0.1"
target_host6 = '::1'
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client6 = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)

client.sendto("AAABBBCCC", (target_host, target_port))

data, addr = client.recv(4096)
print(addr)
print(data)
