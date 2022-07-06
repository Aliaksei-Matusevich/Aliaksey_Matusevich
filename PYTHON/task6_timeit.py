from functools import wraps
import time

def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Функция  {func.__name__}{args} - выполняется за {total_time:.6f} секунд')
        return result
    return timeit_wrapper

@timeit
def counting_time(n):
    total = sum(range(n))
    return total

counting_time(110000073)