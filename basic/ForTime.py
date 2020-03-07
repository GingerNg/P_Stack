import numpy as np
import time
def mockdata():
    for _ in range(10):
        s = time.time()
        sum = 0
        for i in range(0,100000):
            sum += i
        print(time.time()-s)

def npmock():
    for _ in range(10):
        ars = np.arange(0, 100000, 1)
        s = time.time()
        sum = 0
        for a in ars:
            sum += a
        print(time.time() - s)


if __name__ == '__main__':
    mockdata()
    print("--------")
    npmock()