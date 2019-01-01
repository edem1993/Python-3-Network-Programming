my_var = 10

def my_function():
	print('This is the function isnide the module.')

if __name__ == '__main__':
	"""
	executes only if used as a standalone script
	if this is imported as a module, doesn't go off
	"""
	print('This will be executed')