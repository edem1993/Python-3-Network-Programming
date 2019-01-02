import threading
import time

def myfunction():
	"Function to be executed"
	print("Start a thread")
	time.sleep(3)
	print("End a thread")
	
#Define an empty list of threads
threads = []

#Runs 5 concurrent sessions of myfunction()
for i in range(5)
	myfunction()
	th.start()		#starting the thread
	threads.append(th)
	
# https://www.python.org/dev/peps/pep-0008/