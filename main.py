import threading
from time import sleep

counter = 0

def print_cube(num):
    global counter
    for i in range(5):
        counter += 1
        print(f'\ncounter {counter}\nCub:', num ** 3)
        sleep(1.5)



def print_square(num):
    global counter
    for i in range(5):
        counter += 1
        print(f'\ncounter {counter}\nSquare:', num ** 2)
        sleep(1.8)




t1 = threading.Thread(target=print_cube, args=(10,))
t2 = threading.Thread(target=print_square, args=(10,))
print('test')

t1.start()
t2.start()
print('test2')
t1.join()
t2.join()
print('test3')
print('end')