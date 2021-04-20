import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func) 
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1 start
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2 stop
        run_time = end_time - start_time    # 3 time calculation
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer
