import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(func):
    def wrapper():
        initial_time = time.time()
        func()
        final_time = time.time()
        print(f"{func.__name__} run speed: {final_time - initial_time}s")

    wrapper()


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


