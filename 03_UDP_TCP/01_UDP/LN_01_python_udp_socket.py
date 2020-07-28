import socket

def main():
	# 1.make a socket
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	while True:
		
		send_data = input("input what you want to send: ")	
		
		# 2.send the messgae
		udp_socket.sendto(send_data.encode("utf-8"), ("192.168.0.20", 64704))	

		if send_data =="exit":
			break
		
	# 3.close the socket
	udp_socket.close()	

if __name__ == "__main__":
	main()
