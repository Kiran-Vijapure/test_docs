import threading
import time

def task1():
	print(f"Doing some task t1")

def task2():
	while True:
		print(f"Doing some task t2")
		time.sleep(3)

if __name__ == '__main__':
	
	t1 = threading.Thread(target=task1)
	t2 = threading.Thread(target=task2)

	t1.start()
	t2.start()

	t1.join()
	t2.join()

	
