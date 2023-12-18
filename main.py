import threading

def print_cube(num):
    print("Куб:", num * num * num)

def print_square(num):
    print("Квадрат:", num * num)

t1 = threading.Thread(target=print_cube, args=(10,))
t2 = threading.Thread(target=print_square, args=(10, ))
t1.start()
t2.start()
t1.join()
t2.join()
print("Готово!")