from functools import partial
from functools import wraps

def priority(a,b):
    def final_decro(func):
        @wraps(func)
        async def wait_func(*args, c=10, **kwargs):
            pass
        return wait_func
    return final_decro

def log(message, level):
    print(f'[{level}] {message}')

error_log = partial(log, level='ERROR')

print(1)
