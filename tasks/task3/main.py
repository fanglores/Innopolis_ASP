'''
Разработать класс для определения типа к которому относится объект, определенный при помощи гистограммы при помощи метода ближайших соседей.
Предположим у нас есть объекты нескольких, например двух, классов. Для каждого из классов мы берем несколько объектов, вычисляем для них гистограммы и записываем в файл (базу)  информацию в виде тип + гистограмма. Дальше у нас есть новый объект (мы тоже вычислили для него гистограмму). Надо узнать к какому классу он относится.
Для отнесения к классу возможно посчитать расстояние между гистограммой нового объекта и всеми гистограммами, которые есть в файле.
Дальше берем три гистограммы из файла для которых расстояние минимальное. Смотрим какого типа большинство - такого типа и новый объект.

Разработать класс NNClassifier который будет выполнять следующие функции:
- читать из текстового файла данные о существующих известных объъектам (Для каждого объекта данные включают Тип объекта, гистограмма)
- позволяют определить на основе гистограммы тип нового объекта
'''

class NNClassifier:
    def __init__(self, path):
        self.objects = self.__readObjects__(path)

    # initial read method
    def __readObjects__(self, path):
        out = []
        f = open(path, "r")

        for line in f.readlines():
            if (not line):
                print('[WARNING] The file seems empty. Skipping.')
                continue
            name = line.split(':')[0]
            hist = [int(x) for x in (line.split(':')[1]).split(',')]
            out.append([name, hist])

        f.close()
        return out

    # distance calculation method
    def __histDistance__(self, h1, h2) -> float:
        if (len(h1) != len(h2)):
            print('[ERROR] Cannot calculate distance due to different dimension of the histograms!')
            return -1

        summ = 0
        for i in range(len(h1)):
            summ += (h1[i] - h2[i]) ** 2

        return summ ** 0.5

    # build a distance dictionary, take the closest type
    def getType(self, hist):
        dist = []
        for obj in self.objects:
            dist.append([self.__histDistance__(hist, obj[1]), obj[0]])

        return min(dist)[1]


if __name__ == '__main__':
    clsr = NNClassifier("C:/text.txt")
    print(clsr.getType([1, 2, 3]))
