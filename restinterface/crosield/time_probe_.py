import time

def time_probe(func):
    """Decorator to measure the execution time of a function."""
    execution_times = []
    
    def wrapper(*args, **kwargs):
        execution_times.clear() # 2024.4.7 init
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_times.append(end_time - start_time)
        return result
    
    def get_execution_times():
        return execution_times
    
    def get_total_time():
        return sum(execution_times)
    
    wrapper.get_execution_times = get_execution_times
    wrapper.get_total_time = get_total_time
    return wrapper