import socket

def main():
	# 1. create a client socket
	tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# 2. get the server ip and port
	server_ip = input("Input server ip: ")
	server_port = int(input("Input server port: "))

	# 3. connect server
	tcp_client_socket.connect((server_ip,server_port))

	# 4. input the file want to download
	download_file_name = input("Input download file name: ")

	# 5. send the download file name to server
	tcp_client_socket.send(download_file_name.encode("utf-8"))

	# 6. receive the data
	download_data =tcp_client_socket.recv(1024 * 1024)

	# 7. write the data to a file
	with open("[new]"+ download_file_name, "wb") as f:
		f.write(download_data)

	# 8. close client socket
	tcp_client_socket.close()


if __name__ == '__main__':
	main()