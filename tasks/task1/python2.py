''''
Задание для самостоятельной работы (на python).
1. Написать функцию для заполнения массива из 1 000 000 элементов целыми числами от 0 до 999
2. Написать функцию подсчета частоты вхождения элементов в интервалы (создать массив на 10 элементов, содержащий гистограмму распределения на 10 интервалов).
    Интервалы: 0—99,  100—199, … ,900—999)
3. Определить длительность работы функции calcHist. Выполнить функцию calcHist 100 раз и получить максимальное, минимальное и среднее время вычисления
4. Создать docker контейнер для вычисления данной задачи
5. Выложить проект на github, прислать ссылку    
''''

import time
import random

def initListWithRandomNumbers():
    rand_list=[]
    n = 1000
    for i in range(n):
        rand_list.append(random.randint(0,999))
    return rand_list

def calcSumm(arr):
    summ = 0
    for val in arr:
        summ = summ + val
    return summ

a = initListWithRandomNumbers()
# starting time
start = time.time()
calcSumm(a)
# end time
end = time.time()
# total time taken
print("Runtime of the calcSumm is ",(end - start))
