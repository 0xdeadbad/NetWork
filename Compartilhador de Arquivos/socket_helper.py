import struct
from time import sleep

class socket_helper:
	
	def __init__(self, app):
		
		self.app = app
	
	def send_msg(self, sock, msg, msgtype, adic=999):
		# Prefix each message with a 4-byte length (network byte order)
		msg = struct.pack('>I', len(msg)) + struct.pack('>I', msgtype) + struct.pack('>I', adic)  + msg
		sock.sendall(msg)

	def recv_msg(self, sock):
		# Read message length and unpack it into an integer
		raw_msg = self.recvall(sock, 12)
		if not raw_msg:
			return None
		msglen = struct.unpack('>I', raw_msg[:4])[0]
		msgtype = struct.unpack('>I', raw_msg[4:8])[0]
		adic = struct.unpack('>I', raw_msg[8:])[0]
		# Read the message data
		return (self.recvall(sock, msglen), msgtype, adic)

	def recvall(self, sock, n):
		# Helper function to recv n bytes or return None if EOF is hit
		data = b''
		progress = 0
		while len(data) < n:
			packet = sock.recv(n - len(data))
			if not packet:
				return None
			data += packet
			self.app.get_widget('downProgress')['value'] = (100*len(data))/n
		return data
