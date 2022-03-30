
import math
import random

'''
A list of Python functions
that I use on a regular basis.
This list is always getting more
and more and more functions...

-Ben

Close All: Ctrl + K + 0
Open All: Ctrl + K + J

'''

def map(value, low1, high1, low2, high2) -> float:
    return low2 + (high2 - low2) * (value - low1) / (high1 - low1)

def clamp(value, low, high) -> float:
    return max(min(value, high), low)

def normalize(value, low, high) -> float:
    return map(value, low, high, 0, 1)

def binormalRand(x = 1) -> float:
    return x * (random.random() * 2 - 1)

def expectedValue(l) -> float:
    return sum(l) / len(l)

def variancePopulation(l) -> float:
    return expectedValue([(x - expectedValue(l)) ** 2 for x in l])

def varianceSample(l) -> float:
    return sum([(x - expectedValue(l)) ** 2 for x in l]) / (len(l) - 1)
    
def standardDeviation(l) -> float:
    return math.sqrt(variancePopulation(l))

def collapseList(lst) -> list:
    new_list = []
    for i in lst:
        if(type(i) == list):
            new_list.extend(collapseList(i))
        else:
            new_list.append(i)
    return new_list

def raiseList(l, row_length) -> list:
    if(len(l) % row_length != 0):
        raise Exception("List length must be divisible by row length")

    new_list = []
    for i in range(int(len(l) / row_length)):
        temp = []
        for j in range(row_length):
            temp.append(l[i * row_length + j])
        new_list.append(temp)   
    return new_list

def Ndistance(l1, l2) -> float:
    if(len(l1) != len(l2)):
        raise Exception("Lists must be the same length")
    return math.sqrt(sum([(x - y) ** 2 for x, y in zip(l1, l2)]))

def roundTo(x, n) -> float:
    return round(x * 10 ** n) / 10 ** n

def sampleReplacement(l, n) -> list:
    return random.sample(l, n)

def sampleUniqueList(l, n) -> list:

    if(len(l) < n):
        raise Exception("List must be longer than number of samples")

    new_list = []
    while len(new_list) < n:
        r = random.choice(l)
        if r not in new_list:
            new_list.append(r)

    return new_list

def sampleUniqueListFromBounds(low, high, n) -> list:
    return sampleUniqueList(range(low, high + 1), n)

'''
Useful for:
- Introducing noise to a list for a Genetic Algorithm
'''
def jitter(l, n) -> list:
    return [x + binormalRand(n) for x in l]

def weightedAverage(l, a) -> float:
    return sum([x * a[i] for i, x in enumerate(l)]) / sum(a)

def normalizeList(l) -> list:
    return [x / sum(l) for x in l]

def cumulativeSum(l) -> list:
    return [sum(l[:i + 1]) for i in range(len(l))]












