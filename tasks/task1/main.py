'''
Задание для самостоятельной работы (на python).
1. Написать функцию для заполнения массива из 1 000 000 элементов целыми числами от 0 до 999
2. Написать функцию подсчета частоты вхождения элементов в интервалы (создать массив на 10 элементов, содержащий гистограмму распределения на 10 интервалов).
    Интервалы: 0—99,  100—199, … ,900—999)
3. Определить длительность работы функции calcHist. Выполнить функцию calcHist 100 раз и получить максимальное, минимальное и среднее время вычисления
4. Создать docker контейнер для вычисления данной задачи
5. Выложить проект на github, прислать ссылку    
'''

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
 

if __name__ == '__main__':
    random.seed(time.time())
    
    num = 100
    arr_size = int(1e6)
    
    a = []
    time_arr = []

    a = initListWithRandomNumbers(arr_size) 
    for i in range(num):
        start = time.time()
        a = calcHist(a)
        end = time.time()

        time_arr.append(end - start)
    
    print("Latest given histogram:", a)
    print("\nAverage time taken:", mean(time_arr))
    print("Minimum time taken:", min(time_arr))
    print("Minimum time taken:", max(time_arr))
