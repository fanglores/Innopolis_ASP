''''
Задание для самостоятельной работы (на python).
1. Написать функцию для заполнения массива из 1 000 000 элементов целыми числами от 0 до 999
2. Написать функцию подсчета частоты вхождения элементов в интервалы (создать массив на 10 элементов, содержащий гистограмму распределения на 10 интервалов).
    Интервалы: 0—99,  100—199, … ,900—999)
3. Определить длительность работы функции calcHist. Выполнить функцию calcHist 100 раз и получить максимальное, минимальное и среднее время вычисления
4. Создать docker контейнер для вычисления данной задачи
5. Выложить проект на github, прислать ссылку    
''''

def calcHist(tdata):
#   hist is a List to store histogram. It contains [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    hist = [0]*10
#   TODO
#   Calculate histogram for tdata List
#   hist [0] = number of values in tdata from 0..99 
#   hist [1] = number of values in tdata from 100..199
#   hist [2] = number of values in tdata from 200..299
#   ...
#   hist [9] = number of values in tdata from 900..sys.maxint
    return hist
#   data contains List with size 1000 000 with 0 values
data = [0]*1000000
a = calcHist(data)
print(a)
