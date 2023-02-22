from type import Point, TwoPointDistance
import math

def minimumTwoPointDistance(listPoint: list[Point]) -> TwoPointDistance:
    return divide(listPoint, 0, len(listPoint)-1)

def divide(listPoint: list[Point], firstI: int, lastI: int) -> TwoPointDistance:
    tmpRes1 : TwoPointDistance
    tmpRes2 : TwoPointDistance
    resMinDistance : TwoPointDistance
    if(firstI==lastI):
        resMinDistance = TwoPointDistance(float('inf'),firstI, firstI)
    elif(firstI+1==lastI):
        resMinDistance = TwoPointDistance(distance(listPoint[firstI], listPoint[lastI]),firstI,lastI)
    else:
        mid: int = (firstI+lastI)//2
        tmpDistance : float
        tmpRes1 = divide(listPoint, firstI, mid)
        tmpRes2 = divide(listPoint, mid+1, lastI)
        if(tmpRes1.distance<tmpRes2.distance):
            resMinDistance = tmpRes1
        else: 
            resMinDistance = tmpRes2
        for i in range(firstI, mid+1):
            for j in range(mid+1, lastI+1):
                tmpDistance = distance(listPoint[i], listPoint[j])
                if(tmpDistance<resMinDistance.distance):
                    resMinDistance = TwoPointDistance(tmpDistance, i, j)
    return resMinDistance

def distance(point1: Point, point2: Point) -> float:
    sum: int = 0
    for i in range(point1.dimension):
        sum += (point1.values[i]-point2.values[i])**2
    return math.sqrt(sum)