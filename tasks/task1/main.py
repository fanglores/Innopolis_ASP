import time
import random

def initListWithRandomNumbers(size):
    rand_list = []
    
    for i in range(size):
        rand_list.append(random.randint(0, 999))
        
    return rand_list

def calcHist(tdata):
    hist = [0]*10
    
    for i in tdata:
        ind = i // 100
        if (ind > 9): ind = 9
            
        hist[ind] += 1

    return hist

def calcSum(arr):
    summ = 0
    
    for val in arr:
        summ += val
        
    return summ
  
if __name__ == '__main__':
    random.seed(time.time())
    
    num = 100
    arr_size = int(1e6)
    
    a = []
    time_arr = []
    for i in range(num):
        a = initListWithRandomNumbers(arr_size)

        start = time.time()
        calcHist(a)
        end = time.time()

        time_arr.append(end - start)
    
    print("Latest given histogram:", a)
    print("\nAverage time taken:", calcSum(time_arr)/num)
    print("Minimum time taken:", min(time_arr))
    print("Minimum time taken:", max(time_arr))
