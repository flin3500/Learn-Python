import socket

def serve_client(serve_socket):
	"""serve client"""

	# 1. get the http request 
	request = serve_socket.recv(1024)

	# 2. pass http file to client
	response = "HTTP/1.1 200 OK\r\n"
	response += "\r\n"
	response += "<h1>21321321321312</h1>"
	serve_socket.send(response.encode("utf-8"))

	# 3. close the serve socket
	serve_socket.close()





def main():
	# 1. make a listen socket
	listen_socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	# 2. bind
	listen_socket.bind(("",9300))

	# 3. listen
	listen_socket.listen(128)

	while True:

		# 4. make a serve socket after accept
		serve_socket, client_address = listen_socket.accept()

		# 5. serve the client
		serve_client(serve_socket)

	# 7. close listen socket
	listen_socket.close()


 
if __name__ == "__main__":
 	main()