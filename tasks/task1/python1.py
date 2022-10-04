'''
Задание для самостоятельной работы (на python).
1. Написать функцию для заполнения массива из 1 000 000 элементов целыми числами от 0 до 999
2. Написать функцию подсчета частоты вхождения элементов в интервалы (создать массив на 10 элементов, содержащий гистограмму распределения на 10 интервалов).
    Интервалы: 0—99,  100—199, … ,900—999)
3. Определить длительность работы функции calcHist. Выполнить функцию calcHist 100 раз и получить максимальное, минимальное и среднее время вычисления
4. Создать docker контейнер для вычисления данной задачи
5. Выложить проект на github, прислать ссылку    
'''

def calcHist(tdata):
#   hist is a List to store histogram. It contains [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    hist = [0]*10
    
    for i in tdata:
        ind = i // 100
        if (ind > 9): ind = 9
            
        hist[ind] += 1

    return hist

if __name__ == '__main__':
    #   data contains List with size 1 000 000 with 0 values
    data = [0]*1000000
    
    # init data with randow values
    for i in data:
        i = random.randint(0, 999)
    
    # execute function
    a = calcHist(data)
    print(a)
