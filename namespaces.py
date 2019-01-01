"""print(list(range(10)), end="\n\n\n")

my_var = 10

try:
	print(my_var)
except NameError as e:
		print(e, "wrong name")
else:
	print("goes out if try works")
finally:
	print("works regardless of anything\n")
"""
"""
my_var = 5

def my_var_func():
	global my_var
	print(my_var)
	my_var = 10
	
my_var_func()
"""

def my_var_func():
	my_var = 10
	print(my_var)
	return my_var
	
result = my_var_func()
	
print(result * 10)