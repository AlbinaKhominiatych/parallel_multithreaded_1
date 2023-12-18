import threading

# Створення демонстраційних потоків (для прикладу)

def worker():
    print("Worker thread is executing")

# Запуск декількох робітників

for i in range(5):
    t = threading.Thread(target=worker)
    t.start()

# Вивід списку всіх живих потоків

current_threads = threading.enumerate()
 for thread in current_threads:
    print(f"Thread Name: {thread.name}. Alive: {thread.is_alive()}")
