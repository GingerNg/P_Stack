
import time
def mockdata():
    for _ in range(10):
        s = time.time()
        sum = 0
        for i in range(0,1000000):
            sum += i
        print(time.time()-s)


if __name__ == '__main__':
    mockdata()