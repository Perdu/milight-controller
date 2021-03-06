#!/usr/bin/env pythonw
# -*- coding: utf-8 -*- 

import config
import socket
import threading

def open_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", config.socket_port))
    return sock

def send_packet(p):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(p, (config.bridge_ip, config.bridge_port))
    except socket.error:
        print "Error sending packet to socket:", p

def simulate_bridge():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", 48899))
    while 1:
        data, addr = sock.recvfrom(1024)
        if data == "Link_Wi-Fi":
            sock.sendto(config.own_ip + ",0000B00B0000" , addr)

def main():
    # Which IP targets which lamp
    cur_target_by_ip = {}
    cur_target = None
    last_ip = None
    cur_ip = None
    t = threading.Thread(target=simulate_bridge)
    t.daemon = True
    t.start()
    s = open_socket()
    while 1:
        data, addr = s.recvfrom(10)
        command = data.encode("hex")
        cur_ip = addr[0]
        target = command[0:2]
        target_command = True
        cur_target = None
        if target == "41" or target == "42":
            cur_target = 0 # all
        if target == "45" or target == "46":
            cur_target = 1
        elif target == "47" or target == "48":
            cur_target = 2
        elif target == "49" or target == "4a":
            cur_target = 3
        elif target == "4b" or target == "4c":
            cur_target = 4
        else:
            target_command = False
        #print last_ip, cur_ip, target_command, cur_target_by_ip
        if last_ip != None and cur_ip != last_ip and not target_command and cur_ip in cur_target_by_ip and cur_target_by_ip[last_ip] != cur_target_by_ip[cur_ip]:
            # We need to add a packet to target correct lamp
            t = cur_target_by_ip[cur_ip]
            if t == 0:
                new_command = "4200"
            elif t == 1:
                new_command = "4500"
            elif t == 2:
                new_command = "4700"
            elif t == 3:
                new_command = "4900"
            elif t == 4:
                new_command = "4b00"
            print "Inserting: " + new_command
            send_packet(new_command.decode("hex"))
        print cur_ip, command
        # Pass receive packet to bridge
        send_packet(data)
        if cur_target != None:
            cur_target_by_ip[cur_ip] = cur_target
        elif cur_ip not in cur_target_by_ip:
            # By default, send command to all lamps
            cur_target_by_ip[cur_ip] = 0
        last_ip = cur_ip

if __name__=='__main__':
    main()
