#практика
"""Завдання на обробку даних: Створити програму,
яка використовує threading.Thread для паралельної
обробки даних у великому списку. Наприклад, розрахунок
середнього значення, медіани, чи сортування великого масиву чисел."""
import threading
import random

#функція обчислення середнього значення
def calculate_mean(arr):
    mean = sum(arr) / len(arr)
    return mean
#великий масив данних
data_size = 10000
data = [random.randint(0, 1000) for _ in range(data_size)]

num_threads = 4
chunk_size = len(data) // num_threads
chunks = [data[i: i + chunk_size] for i in range(0, len(data), chunk_size)]
results = []
#створення потоків
threads = []
for chunk in chunks:
    thread = threading.Thread(target=lambda x: results.append(calculate_mean(x)),
                              args=(chunk, ))
    threads.append(thread)
    print(0,thread)
    thread.start()
#чекаємо завершення кожного потоку
print(1, threads)
for thread in threads:
    thread.join()
print(2,threads)
#загальне середнє значення
total_mean = sum(results) / len(results)
print("Результат: ", {total_mean})