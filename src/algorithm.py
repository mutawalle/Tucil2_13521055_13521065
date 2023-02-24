from type import Point, TwoPointDistance
import math
import time

def bruteForce(listPoint: list[Point]) -> TwoPointDistance:
    # Algoritma Brute Force
    # mencari jarak terdekat dengan mencoba semua kemungkinan dari point yang ada
    if (len(listPoint) == 1):
        return TwoPointDistance(float('inf'),firstI, firstI)
    else:
        resMinDistance : float = TwoPointDistance(distance(listPoint[0], listPoint[1]), 0, 1)

        for i in range(len(listPoint)):
            for j in range(i + 1, len(listPoint)):
                if distance(listPoint[i], listPoint[j]) < resMinDistance.distance:
                    resMinDistance = TwoPointDistance(distance(listPoint[i], listPoint[j]), i, j)

        return resMinDistance


def minimumTwoPointDistance(listPoint: list[Point]) -> (TwoPointDistance, list[Point]):
    # Menghasilkan TwoPointDistance yang berisi
    # distance, indeks Point 1, indeks Point 2

    # Pre-processing
    # List terurut berdasarkan x (dimensi pertama)
    P = sorted(listPoint, key=lambda Point: Point.values[0])

    return (divide(P, 0, len(P)-1), P)

def stripClosest(strip: list[Point], stripIndex: list[int], minDistance: TwoPointDistance) -> TwoPointDistance:
    # Menghasilkan TwoPointDistance pada Strip Area
    min_distance : float = minDistance.distance
    resMinDistance : TwoPointDistance = minDistance

    # Pre-processing
    # List terurut berdasarkan y (dimensi kedua)
    combined = zip(strip, stripIndex)
    combined = sorted(combined, key = lambda x: x[0].values[1])
    stripIndex = [y for x,y in combined]
    strip = [x for x,y in combined]
    # strip = sorted(strip, key = lambda Point: Point.values[1])

    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            # Jika saat perbandingan indeks dan indeks setelahnya sudah lebih dari
            # distance, maka break karena untuk indeks2 selanjutnya pasti > min_distance
            if (strip[j].values[1] - strip[i].values[1] >= min_distance):
                break

            # Jika lebih kecil, update
            if distance(strip[i], strip[j]) < min_distance:
                min_distance = distance(strip[i], strip[j])
                resMinDistance = TwoPointDistance(distance(strip[i], strip[j]), stripIndex[i], stripIndex[j])        

    return resMinDistance

def divide(listPoint: list[Point], firstI: int, lastI: int) -> TwoPointDistance:
    # Kamus lokal
    tmpRes1 : TwoPointDistance
    tmpRes2 : TwoPointDistance
    resMinDistance : TwoPointDistance

    # Jika first index = last index
    # Kasus jumlah elemen = 1
    if(firstI==lastI):
        return TwoPointDistance(float('inf'),firstI, firstI)
    # Kasus jumlah elemen = 2
    elif(firstI+1==lastI):
        return TwoPointDistance(distance(listPoint[firstI], listPoint[lastI]),firstI,lastI)
    # Kasus lain
    else:
        # Bagi 2 bagian left, right
        mid: int = (firstI+lastI)//2
        midPoint: Point = listPoint[mid]
        tmpDistance : float

        # RECURSIVE
        # tmpRes1 bagian kiri
        tmpRes1 = divide(listPoint, firstI, mid)
        # tmpRes2 bagian kanan
        tmpRes2 = divide(listPoint, mid+1, lastI)

        # Menentukan minimum distance
        if(tmpRes1.distance<tmpRes2.distance):
            resMinDistance = tmpRes1
        else: 
            resMinDistance = tmpRes2

        # Meninjau kasus pada Strip Area
        strip: list[Point] = []
        stripIndex: list[int] = []
        for i in range(firstI, lastI + 1):
            if abs(listPoint[i].values[0] - midPoint.values[0]) < resMinDistance.distance:
                strip.append(listPoint[i])
                stripIndex.append(i)
        
        resStripDistance : TwoPointDistance = stripClosest(strip, stripIndex, resMinDistance)

        if (resMinDistance.distance < resStripDistance.distance):
            return resMinDistance
        else:
            return resStripDistance
        # for i in range(firstI, mid+1):
        #     for j in range(mid+1, lastI+1):
        #         tmpDistance = distance(listPoint[i], listPoint[j])
        #         if(tmpDistance<resMinDistance.distance):
        #             resMinDistance = TwoPointDistance(tmpDistance, i, j)

def distance(point1: Point, point2: Point) -> float:
    sum: int = 0
    for i in range(point1.dimension):
        sum += (point1.values[i]-point2.values[i])**2
    return math.sqrt(sum)