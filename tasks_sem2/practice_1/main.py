import re
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from math import sqrt


def ReadTextFromFile(filename):
    try:
        text = None
        with open(filename, mode='r', encoding='utf-8') as f:
            text = f.readlines()
            f.close()

        # join separate lines into one string
        text = ' '.join(text)
        text = text.lower()
        return text
    except Exception as e:
        print(f'Critical error while opening or reading a file! {type(e)}: {str(e)}')

def WordFrequency(text):
    text = re.sub('[^А-Яа-я0-9]+', ' ', text)

    new_tokens = word_tokenize(text)
    new_tokens = [t for t in new_tokens if t not in stopwords.words('russian')]

    word_freq = nltk.FreqDist(new_tokens)

    return dict(word_freq)

def GetEuclidDistance(a, b):
    keysList = list(a.keys())
    keysList.extend(list(b.keys()))

    keysSet = set()
    for key in keysList:
        keysSet.add(key)

    distance = 0.0
    for i in keysSet:
        a_val, b_val = a.get(i), b.get(i)

        if a_val is None:
            a_val = 0
        if b_val is None:
            b_val = 0

        distance += (a_val - b_val)**2

    return sqrt(distance)

def Analyze(filename):
    text = ReadTextFromFile(filename)
    return WordFrequency(text)

def DefineTypeByNeighbours(data, class1, class2):
    NUM_NEIGHBOURS = 3

    distances = dict()
    for i in range(len(class1)):
        distances[f'1_{i}'] = GetEuclidDistance(data, class1[i])

    for i in range(len(class2)):
        distances[f'2_{i}'] = GetEuclidDistance(data, class2[i])

    distances = sorted(distances.items(), key=lambda x: x[1])

    count = 0
    for i in range(NUM_NEIGHBOURS):
        if distances[i][0][0] == '2':
            count += 1

    return (2 if count > NUM_NEIGHBOURS // 2 else 1)


if __name__ == '__main__':
    detectivesData = [Analyze(f'dataset\\detective{i+1}.txt') for i in range(5)]
    scifiData = [Analyze(f'dataset\\scifi{i+1}.txt') for i in range(5)]

    testData = Analyze('dataset\\testsample.txt')

    print('Test data was recognized as ', 'DETECTIVE' if DefineTypeByNeighbours(testData, detectivesData, scifiData) == 1 else 'SCIFI')