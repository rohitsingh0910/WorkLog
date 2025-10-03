import threading

def print_square(num):
    print(num * num)

threads = []
for i in range(5):
    t = threading.Thread(target=print_square, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
