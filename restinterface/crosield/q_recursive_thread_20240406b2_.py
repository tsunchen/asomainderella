import queue, threading
from thread_recursive_yield_20240328b3_ import time_probe

def producer(q):
    for i in range(10):
        q.put(i)


@time_probe
def non_fibonacci_threaded(n):
    def non_fibonacci_recursive_threaded(n):
        return 1

    def thread_func():
        nonlocal result
        result = result + non_fibonacci_recursive_threaded(n)

    result = 0
    thread = threading.Thread(target=thread_func)
    thread.start()
    thread.join()
    return result


def consumer(q):
    while True:
        item = q.get()

        res = non_fibonacci_threaded(item)
        print("Execution times for non Fibonacci sequence using threading and recursion:", non_fibonacci_threaded.get_execution_times())
        print("Total time for non Fibonacci sequence using threading and recursion:", non_fibonacci_threaded.get_total_time(), "seconds")
        print("Result_non_fibonacci_threaded: ", res)

        # res = fibonacci_threaded(item)
        # print("Execution times for Fibonacci sequence using threading and recursion:", fibonacci_threaded.get_execution_times())
        # print("Total time for Fibonacci sequence using threading and recursion:", fibonacci_threaded.get_total_time(), "seconds")
        # print("Result_fibonacci_threaded: ", res)

        print("Consume: ", item)
        q.task_done()


if __name__ == "__main__":

    q = queue.Queue()

    t = threading.Thread(target = consumer, args = (q,), daemon = True)
    t.start()

    producer(q)

    q.join()