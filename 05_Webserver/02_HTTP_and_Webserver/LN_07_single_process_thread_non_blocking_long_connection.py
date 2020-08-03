import socket
import re

def serve_client(serve_socket, request):
	"""serve client"""

	# 1. get the http request 
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
		response += "Content-Length:%d\r\n" % len(html_content)
		response += "\r\n"

		# 4. send header
		serve_socket.send(response.encode("utf-8"))

		# 5. send body
		serve_socket.send(html_content)





def main():
	# 1. make a listen socket
	listen_socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	# 2. bind
	listen_socket.bind(("",9300))

	# 3. listen
	listen_socket.listen(128)
	listen_socket.setblocking(False)

	serve_socket_list = list()

	while True:

		# 4. make a serve socket after accept
		try:
			serve_socket, client_address = listen_socket.accept()
		except Exception as e:
			pass
		else:
			serve_socket.setblocking(False)
			serve_socket_list.append(serve_socket)

		for serve_socket in serve_socket_list:
			try:
				recv_data = serve_socket.recv(1024).decode("utf-8")
			except Exception as e:
				pass
			else:
				print(recv_data)
				if recv_data:
					# 5. serve lient
					serve_client(serve_socket, recv_data)
				else:
					serve_socket.close()
					serve_socket_list.remove(serve_socket)

	# 7. close listen socket
	listen_socket.close()


 
if __name__ == "__main__":
 	main()