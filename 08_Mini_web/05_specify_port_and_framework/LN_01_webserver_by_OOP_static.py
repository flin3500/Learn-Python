import socket
import re
import multiprocessing
import time
import sys


class WSGIServer(object):


	def __init__(self, port, app, static_path):
		# 1. make a listen socket
		self.listen_socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		# 2. bind
		self.listen_socket.bind(("",port))
		# 3. listen
		self.listen_socket.listen(128)
		self.application = app
		self.static_path = static_path


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
				f = open(self.static_path + file_name,"rb")
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
			env['PATH_INFO'] = file_name
			body = self.application(env, self.set_response_header)
						
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
		self.headers = [("server", "mini_web v8.8")]
		self.headers += headers


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
	if len(sys.argv) == 2:
		try:
			port = int(sys.argv[1])
		except Exception as e:
			return
	elif len(sys.argv) == 3:
		try:
			port = int(sys.argv[1])
			frame_name = sys.argv[2]
		except Exception as e:
			return
	else:
		return

	reg = re.match(r"([^:]+):(.*)", frame_name)
	if reg:
		frame_name = reg.group(1)
		app_name  = reg.group(2)
	else:
		return

	with open("./webserver.conf") as f:
		conf_info = eval(f.read())

	sys.path.append(conf_info["dynamic_path"])
	frame = __import__(frame_name)
	app = getattr(frame, app_name)


	webserver = WSGIServer(port, app, conf_info["static_path"])
	webserver.run_forever()


 
if __name__ == "__main__":
 	main()