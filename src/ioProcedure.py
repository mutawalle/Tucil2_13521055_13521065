from type import Point
import math
import random


def inputProc(n: int, d: int, listPoint: list[Point]):
    n = int(input())
    d = int(input())

    for i in range(n):
        tmpPoint: Point
        tmpValues: list[int] = []
        for i in range(d):
            tmpValues.append(math.floor(random.random()*100))
        tmpPoint = Point(d, tmpValues)
        listPoint.append(tmpPoint)
