"""性能分析"""
import cProfile


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def time_profile_t():
    """
    程序执行时间、函数调用次数分析
    (venv) PS D:\code\python-demo\standard_t> python .\profile_t.py 30
832040
         2692539 function calls (3 primitive calls) in 0.375 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
2692537/1    0.375    0.000    0.375    0.375 profile_t.py:6(fibonacci)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    """
    profile = cProfile.Profile()
    profile.enable()
    fibonacci(30)
    profile.disable()
    profile.print_stats()


if __name__ == '__main__':
    time_profile_t()