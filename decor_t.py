from functools import partial 

def priority_limit_async_func_call(a=1):
    def final_decro(func):
        def wrapper(*args, c=10, **kwargs):
            pass
        return wrapper
    return final_decro

def log(message, level):
    print(f'[{level}] {message}')


r = priority_limit_async_func_call(a=5)(
    partial(log, level='ERROR')
)

print(r)