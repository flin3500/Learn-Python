import socket

def main():
	# 1.make a socket
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# 2.bind a local addr
	local_addr = ("", 7788)
	udp_socket.bind(local_addr)

	# 3.receive message
	while True:
		recv_data = udp_socket.recvfrom(1024)
		recv_msg = recv_data[0]
		send_addr = recv_data[1]

		# 4.print receive recv_data
		#print(recv_data)
		if recv_msg.decode("utf-8")=="exit":
			break
		print("%s %s" % (str(send_addr), recv_msg.decode("utf-8")))


	# 5.close socket
	udp_socket.close()



if __name__ == '__main__':
	main()




