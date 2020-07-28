import socket

def main():
	# 1. make a socket
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# 2. input the dest infomation and data 
	dest_ip = input("Destination IP: ")
	dest_port = int(input("Destination Port:"))
	send_data = input("input what you want to send: ")	
		
	# 3. send the message
	udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))

	# 4. receive the message
	recv_data = udp_socket.recvfrom(1024)
	print(recv_data)

	# 5. close the socket
	udp_socket.close()	

if __name__ == "__main__":
	main()
