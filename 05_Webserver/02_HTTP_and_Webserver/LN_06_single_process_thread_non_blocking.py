import socket
import re

def serve_client(serve_socket):
	"""serve client"""

	# 1. get the http request 
	request = serve_socket.recv(1024).decode("utf-8")
	print(request)
	request_line = request.splitlines()
	ret = re.match(r"[^/]+(/[^ ]*)", request_line[0])
	file_name = ""
	if ret:
		file_name = ret.group(1)
		if file_name == "/":
			file_name = "/index.html"

	# 2. find the file
	try:
		f = open("./html" + file_name,"rb")
	except:
		# 3. header
		response = "HTTP/1.1 404 NOT FOUND\r\n"
		response += "\r\n"
		response += "______FILE_NOT_FOUND_______"

		# 4. send
		serve_socket.send(response.encode("utf-8"))
	else:
		html_content = f.read()
		f.close()

		# 3. header
		response = "HTTP/1.1 200 OK\r\n"
		response += "\r\n"

		# 4. send header
		serve_socket.send(response.encode("utf-8"))

		# 5. send body
		serve_socket.send(html_content)
		

	

	# 6. close the serve socket
	serve_socket.close()





def main():
	# 1. make a listen socket
	listen_socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

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