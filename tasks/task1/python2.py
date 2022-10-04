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

def calcSum(arr):
    summ = 0
    
    for val in arr:
        summ += val
        
    return summ


if __name__ == '__main__':
    time_arr = []
    
    for i in range(100):
        a = initListWithRandomNumbers()

        # starting time
        start = time.time()

        calcSum(a)

        # end time
        end = time.time()

        # total time taken
        time_arr.append(end - start)
    
    print("Average time taken:", calcSum(time_arr)/100)
    print("Minimum time taken:", min(time_arr))
    print("Minimum time taken:", max(time_arr)
