import ntpath
from classes import *
			
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)	

def add_file(cls, dict_name):
	
	file_path = af()
	lb = cls.get_widget(dict_name)
	lb.insert(lb.size(), path_leaf(file_path))
		
if __name__ == '__main__':
	
	app = Application('Client')
	soc = Socket_tcp.Client(app)

	app.add_widget(item=tk.Label, name='progressLabel', args=dict(text='Progress:'))
	app.add_widget(item=ttk.Progressbar, name='downProgress', args=dict(orient="horizontal", mode="determinate"))
	app.add_widget(item=tk.Listbox, name='filesBox')
	app.add_widget(item=tk.Button, name='downButton', args=dict(text='Download', command=lambda: soc.request_file(app.get_widget('filesBox').curselection()[0])))
	#app.add_widget(item=tk.Button, name='addButton', args=dict(text='Add File', command=lambda: (add_file(app, 'filesBox'))))
	print(app.items)
	app.pack_all()
	
	soc.connect(('localhost', 22122))
	app.start()
	
