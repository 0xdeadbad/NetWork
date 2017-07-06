import ntpath
from classes import *
			
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)	

def add_file(cls, dict_name, server):
	
	file_path = af()
	lb = cls.get_widget(dict_name)
	lid = lb.size()
	lb.insert(lid, path_leaf(file_path))
	cls.files[lid] = file_path
	server.send_update()
		
if __name__ == '__main__':
	
	app = Application('Server')
	soc = Socket_tcp.Server(app, addr=('172.16.102.9', 22122))
	listen_thread = Th(soc.listen)
	#ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate"
	app.add_widget(item=tk.Label, name='progressLabel', args=dict(text='Progress:'))
	app.add_widget(item=ttk.Progressbar, name='downProgress', args=dict(orient="horizontal", mode="determinate"))
	app.add_widget(item=tk.Listbox, name='filesBox')
	#app.add_widget(item=tk.Button, name='downButton', args=dict(text='Download', command=lambda: (print(app.get_widget('filesBox').get(app.get_widget('filesBox').curselection())))))
	app.add_widget(item=tk.Button, name='addButton', args=dict(text='Add File', command=lambda: (add_file(app, 'filesBox', soc))))

	app.pack_all()
	
	

	listen_thread.start()
	app.start()
