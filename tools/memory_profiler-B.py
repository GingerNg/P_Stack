from memory_profiler import profile

"""
https://github.com/pythonprofilers/memory_profiler
"""

"""
 the second column (Mem usage) the memory usage of the Python interpreter after that line has been executed. 
 The third column (Increment) represents the difference in memory of the current line with respect to the last one. 
"""
@profile(precision=4)
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a

if __name__ == '__main__':
    my_func()