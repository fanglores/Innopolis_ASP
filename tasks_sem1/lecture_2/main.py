'''
Задание к лекции 2
1. Разработать функцию, которая будет использовать операцию цикла для рисования равнобедренного треугольника при помощи звездочек (*)
2. Разработать функцию для вычисления декартова расстояния между гистограммами (Гистограмма это вектор размерности n. Расстояние между гистограммами можно вычислить, как расстояние между n-мерными векторами)
3. Разработать функцию для записи гистограмм в файл
4. Разработать функцию для чтения гистограмм из файла
5. Создать docker контейнер для вычисления данной задачи
5. Выложить проект на github, прислать ссылку (просьба поместить вторую задачу в папку с именем task2)
'''


def triangle(a):
    for i in range(a, -1, -1):
        print(' '*i + '*'*((a - i)*2 + 1))

def histDistance(h1, h2) -> float:
    if (len(h1) != len(h2)):
        print('[ERROR] Cannot calculate distance due to different dimension of the histograms!')
        return -1
    else:
        sum = 0
        
        for i in range(len(h1)):
            sum += (h1[i] - h2[i])**2
            
        return sum**0.5

def readHist(path, separator = ','):
    f = open(path, "r")
    
    line = f.readline()
    if(not line):
        print('[WARNING] The file seems empty.')
        return -1
    hist = [int(x) for x in line.split(separator)]
    
    f.close()
    return hist

def writeHist(path, h, separator = ','):
    f = open(path, "w")

    line = [str(x) for x in h]
    line = separator.join(line)
    f.write(line)
    
    f.close()


if __name__ == '__main__':
    print('triangle(3):')
    triangle(3)
    print('\n\n')
    
    print('histDistance([1,2,3], [0,0,0])^2:', histDistance([1,2,3], [0,0,0])**2, '\n\n')

    path = "C:\\txt.txt"
    print('Read histogram:', readHist(path))
    t_hist = [0,3,2,1]
    print('Wrote histogram:', t_hist)
    writeHist(path, t_hist)
    print('Read histogram:', readHist(path)) 
  
