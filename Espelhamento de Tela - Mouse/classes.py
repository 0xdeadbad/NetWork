from threading import Thread

class Th(Thread):
	
	def __init__(self, func, args=()):
		Thread.__init__(self)
		self.func = func
		self.args = args
	
	def run(self):
		self.func(*self.args)
