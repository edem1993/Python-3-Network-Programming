"""
try:
	code
except:
	code
"""

for i in range(5):
	try:
		print(i / 0)
	except ZeroDivisionError as e:
		print(e, "--> Division by 0 is just wrong")
	except NameError:
		print("Name error detected!")
	except ValueError:
		print("Wrong value!")
#	print("The rest of the code...")
		
		
try:
    print(4/0) #in the "try" clause you insert the code that you think might generate an exception at some point
except ZeroDivisionError:
    print("Division Error!") #specifying what exception types Python should expect as a consequence of running the code inside the "try" block and how to handle them
else:
    print("No exceptions raised by the try block!") #executed if the code inside the "try" block raises NO exceptions
finally:
    print("I don't care if an exception was raised or not!") #executed whether the code inside the "try" block raises an exception or not
