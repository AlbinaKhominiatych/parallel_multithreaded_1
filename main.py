import threading
from time import sleep

counter = 0


def print_cube(num):
    global counter
    while True:
        counter += 1
        print(f'\ncounter {counter}\nCub:', num ** 3)
        sleep(1.5)


def print_square(num):
    global counter
    while True:
        counter += 1
        print(f'\ncounter {counter}\nSquare:', num ** 2)
        sleep(1.8)


t1 = threading.Thread(target=print_cube, args=(10,))
t2 = threading.Thread(target=print_square, args=(10,))
print('test')




t1.start()
t2.start()


print('test2')

current_threads = threading.enumerate()
for thread in current_threads:
    print(f"Thread Name: {thread.name}. Alive: {thread.is_alive()}")


t1.join()
t2.join()
print('test2')
print('end')