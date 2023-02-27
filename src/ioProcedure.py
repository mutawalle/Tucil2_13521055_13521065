from type import Point
import math
import random

def inputProc(n: int, d: int, listPoint: list[Point]):
    # n : banyak point
    n = int(input())

    # d : dimensi
    d = int(input())

    while (len(listPoint) < n):
        tmpPoint: Point
        tmpValues: list[float] = []
        for i in range(d):
            tmpValues.append(round(random.uniform(-1000, 1000), 2))
        tmpPoint = Point(d, tmpValues)
        
        # check agar tidak duplikat
        if (tmpPoint not in listPoint):
            listPoint.append(tmpPoint)

def printResPoint(listPoint: list[Point], index: int):
    print("<", end = '')
    for i in range (listPoint[0].dimension):
        print(listPoint[index].values[i], end = '')
        if (i != listPoint[0].dimension - 1):
            print(',', end = '')
    print(">")
