import socket
import re
import multiprocessing
import time
import LN_02_WSGI_frame


class WSGIServer(object):


	def __init__(self):
		# 1. make a listen socket
		self.listen_socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		# 2. bind
		self.listen_socket.bind(("",9300))
		# 3. listen
		self.listen_socket.listen(128)


	def serve_client(self, serve_socket):
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
		if not file_name.endswith(".py"):
			try:
				f = open("../../05_Webserver/02_HTTP_and_Webserver/html" + file_name,"rb")
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
		else:
			"""
			active request
			"""


			env = dict()
			body = LN_02_WSGI_frame.application(env, self.set_response_header)
						
			header = "HTTP/1.1 %s\r\n" % self.status

			for temp in self.headers:
				header += "%s:%s\r\n" % (temp[0],temp[1])

			header += "\r\n"

			response = header+body
			serve_socket.send(response.encode("utf-8"))

			
		# 6. close the serve socket
		serve_socket.close()

	def set_response_header(self, status, headers):
		self.status = status
		self.headers = headers


	def run_forever(self):
		while True:
			# make a serve socket after accept
			serve_socket, client_address = self.listen_socket.accept()
			process1= multiprocessing.Process(target=self.serve_client, args = (serve_socket,))
			process1.start()
			serve_socket.close()

		# close listen socket
		self.listen_socket.close()

def main():
	webserver = WSGIServer()
	webserver.run_forever()


 
if __name__ == "__main__":
 	main()