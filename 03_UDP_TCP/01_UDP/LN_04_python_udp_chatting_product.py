import socket


def sender(udp_socket):
	dest_ip = input("Input the destination ip: ")
	dest_port = int(input("Input the destination port: "))
	send_data = input("Input the message: ")
	udp_socket.sendto(send_data.encode("utf-8"),(dest_ip, dest_port))


def receiver(udp_socket):
	recv_data = udp_socket.recvfrom(1024)
	print("%s:%s" % (str(recv_data[1]),recv_data[0].decode("utf-8")))


def main():
	# make a socket
	udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

	# bind port
	local_port = int(input("Input the port you want to send message: "))
	udp_socket.bind(("",local_port))

	# use a loop to continue chatting
	while True:
		# send
		sender(udp_socket)
		#receive
		receiver(udp_socket)
		

if __name__ == '__main__':
	main()