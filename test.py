import time
from time import clock

def check(num):
    a = list(str(num))
    b = a[::-1]
    if a == b:
        return True
    return False
                                                                                                  
def main():
    all = range(1,10**7)
    for i in all:
        if check(i):
            if check(i**2):
		pass
                print(i,i**2)
   
if __name__ == '__main__':
    start = clock()
    main()
    end = clock()
    print (end-start)

