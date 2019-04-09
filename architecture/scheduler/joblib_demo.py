import time

from joblib import Memory
from joblib import Parallel, delayed

def task1():
    print("---")

def task2(i):
    print(i)

start = time.time()
results = Parallel(n_jobs=2)(delayed(task2) for i in range(10))

stop = time.time()

print('\nFirst round - caching the data')
print('Elapsed time for the entire processing: {:.2f} s'
      .format(stop - start))