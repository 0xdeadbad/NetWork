def check_and_install(*packages):
	flag = False
	for package in packages:
		import importlib
		try:
			importlib.import_module(package)
		except ImportError:
			flag = True
			import pip
			pip.main(['install', package])
	
	return flag
