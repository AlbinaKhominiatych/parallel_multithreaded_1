import threading
from time import sleep

counter = 0

def print_cube(num):
    global counter
    while True:
        print(f'\ncounter {counter}\nCub:', num ** 3)
        sleep(1)
        counter += 1


def print_square(num):
    global counter
    while True:
        print(f'\ncounter {counter}\nSquare:', num ** 2)
        sleep(1.2)
        counter += 1


t1 = threading.Thread(target=print_cube, args=(10,))
t2 = threading.Thread(target=print_square, args=(10,))

t1.start()
t2.start()

t1.join()
t2.join()
print('end')