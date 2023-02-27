from type import Point, TwoPointDistance
import math

countBF = 0
countDNC = 0

def bruteForce(listPoint: list[Point]) -> TwoPointDistance:
    global countBF
    # Algoritma Brute Force
    # mencari jarak terdekat dengan mencoba semua kemungkinan dari point yang ada
    if (len(listPoint) == 1):
        return TwoPointDistance(float('inf'), 0, 0)
    else:
        resMinDistance: float = TwoPointDistance(
            distance(listPoint[0], listPoint[1]), 0, 1)
        countBF += 1

        for i in range(len(listPoint)):
            for j in range(i + 1, len(listPoint)):
                if distance(listPoint[i], listPoint[j]) < resMinDistance.distance:
                    resMinDistance = TwoPointDistance(
                        distance(listPoint[i], listPoint[j]), i, j)
                countBF += 1

        return resMinDistance


def minimumTwoPointDistance(listPoint: list[Point]) -> (TwoPointDistance, list[Point]):
    # Menghasilkan TwoPointDistance yang berisi
    # distance, indeks Point 1, indeks Point 2

    # Pre-processing
    # List terurut berdasarkan x (dimensi pertama)
    mergeSortPoint(listPoint, 0)

    return (divide(listPoint, 0, len(listPoint)-1), listPoint)


def stripClosest(strip: list[Point], stripIndex: list[int], minDistance: TwoPointDistance) -> TwoPointDistance:
    # Menghasilkan TwoPointDistance pada Strip Area
    min_distance: float = minDistance.distance
    resMinDistance: TwoPointDistance = minDistance
    global countDNC

    # Pre-processing
    # List terurut berdasarkan y (dimensi kedua)
    combined = [list(a) for a in zip(strip, stripIndex)]
    # combined = list(zip(strip, stripIndex))
    # print(combined)
    mergeSortZip(combined, 1)

    # combined = zip(strip, stripIndex)
    # combined = sorted(combined, key=lambda x:x[0].values[1])
    stripIndex = [y for x, y in combined]
    strip = [x for x, y in combined]

    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            # Jika saat perbandingan indeks dan indeks setelahnya sudah lebih dari
            # distance, maka break karena untuk indeks2 selanjutnya pasti > min_distance
            if (strip[j].values[1] - strip[i].values[1] >= min_distance):
                break

            # Jika lebih kecil, update
            temp_distance = distance(strip[i], strip[j])
            countDNC += 1
            if temp_distance < min_distance:
                min_distance = temp_distance
                resMinDistance = TwoPointDistance(
                    temp_distance, stripIndex[i], stripIndex[j])

    return resMinDistance


def divide(listPoint: list[Point], firstI: int, lastI: int) -> TwoPointDistance:
    # Kamus lokal
    tmpRes1: TwoPointDistance
    tmpRes2: TwoPointDistance
    resMinDistance: TwoPointDistance
    global countDNC

    # Jika first index = last index
    # Kasus jumlah elemen = 1
    if (firstI == lastI):
        return TwoPointDistance(float('inf'), firstI, firstI)
    # Kasus jumlah elemen = 2
    elif (firstI+1 == lastI):
        countDNC += 1
        return TwoPointDistance(distance(listPoint[firstI], listPoint[lastI]), firstI, lastI)
    # Kasus lain
    else:
        # Bagi 2 bagian left, right
        mid: int = (firstI+lastI)//2
        midPoint: Point = listPoint[mid]

        # RECURSIVE
        # tmpRes1 bagian kiri
        tmpRes1 = divide(listPoint, firstI, mid)
        # tmpRes2 bagian kanan
        tmpRes2 = divide(listPoint, mid+1, lastI)

        # Menentukan minimum distance
        if (tmpRes1.distance < tmpRes2.distance):
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

        resStripDistance: TwoPointDistance = stripClosest(
            strip, stripIndex, resMinDistance)

        if (resMinDistance.distance < resStripDistance.distance):
            return resMinDistance
        else:
            return resStripDistance


def distance(point1: Point, point2: Point) -> float:
    sum: int = 0
    for i in range(point1.dimension):
        sum += (point1.values[i]-point2.values[i])**2
    return math.sqrt(sum)

def mergeSortPoint(listPoint: list[Point], index: int):
    if len(listPoint) > 1:
        mid: int
        i: int
        j: int
        k: int
        lengthLeft: int
        lengthRight: int
        leftHalf: list[Point]
        rightHalf: list[Point]
        # Bagi menjadi 2 bagian
        mid = len(listPoint) // 2
        leftHalf = listPoint[:mid]
        rightHalf = listPoint[mid:]

        # urutkan setiap bagian
        mergeSortPoint(leftHalf, index)
        mergeSortPoint(rightHalf, index)

        # gabung kembali
        i = j = k = 0
        lengthLeft = len(leftHalf)
        lengthRight = len(rightHalf)
        while i < lengthLeft and j < lengthRight:
            if getattr(leftHalf[i], "values")[index] < getattr(rightHalf[j], "values")[index]:
                listPoint[k] = leftHalf[i]
                i += 1
            else:
                listPoint[k] = rightHalf[j]
                j += 1
            k += 1

        while i < lengthLeft:
            listPoint[k] = leftHalf[i]
            i += 1
            k += 1

        while j < lengthRight:
            listPoint[k] = rightHalf[j]
            j += 1
            k += 1


def mergeSortZip(listZip, index: int):
    if len(listZip) > 1:
        mid: int
        i: int
        j: int
        k: int
        lengthLeft: int
        lengthRight: int
        leftHalf: list[Point]
        rightHalf: list[Point]
        # Bagi menjadi 2 bagian
        mid = len(listZip) // 2
        leftHalf = listZip[:mid]
        rightHalf = listZip[mid:]

        # urutkan setiap bagian
        mergeSortZip(leftHalf, index)
        mergeSortZip(rightHalf, index)

        # gabung kembali
        i = j = k = 0
        lengthLeft = len(leftHalf)
        lengthRight = len(rightHalf)
        while i < lengthLeft and j < lengthRight:
            if leftHalf[i][0].values[index] < rightHalf[j][0].values[index]:
                listZip[k] = leftHalf[i]
                i += 1
            else:
                listZip[k] = rightHalf[j]
                j += 1
            k += 1

        while i < lengthLeft:
            listZip[k] = leftHalf[i]
            i += 1
            k += 1

        while j < lengthRight:
            listZip[k] = rightHalf[j]
            j += 1
            k += 1
