import struct
from pickle import loads
from classes import Th

def msg_switch(msg, msgtype, cls):
	
	if msgtype == 0:
		cls.update_image(msg)
	elif msgtype == 1:
		coords = loads(msg)
		cls.update_mouse(coords, 1)
	elif msgtype == 2:
		coords = loads(msg)
		Th(cls.update_mouse, (coords, 2)).start()

def recv_msg(sock, cls):
	
	raw_msg = recvall(sock, 8)
	if not raw_msg:
		return None
	msglen = struct.unpack('>I', raw_msg[0:4])[0]
	msgtype = struct.unpack('>I', raw_msg[4:8])[0]
	print(msgtype)
	
	msg = recvall(sock, msglen)
	
	msg_switch(msg, msgtype, cls)

def recvall(sock, n):
	
	data = b''
	while len(data) < n:
		packet = sock.recv(n - len(data))
		if not packet:
			return None
		data += packet
	return data

def send_msg(sock, msg, msgtype):
	
	msg1 = struct.pack('>I', len(msg))
	msg2 = struct.pack('>I', msgtype)
	nmsg = msg1 + msg2 + msg
	sock.sendall(nmsg)
