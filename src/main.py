# input
# generate n random points pada ruang n
# divide n conquer
# dibagi 2 tiap bagian dicari yang paling dekat, bandingkan antar bagian
# output visualisasi

from type import Point, TwoPointDistance
from ioProcedure import inputProc
from algorithm import minimumTwoPointDistance

n: int = 0
d: int = 0
listPoint: list[Point] = []
result : TwoPointDistance

inputProc(n, d, listPoint)
result = minimumTwoPointDistance(listPoint)

print(result.distance, result.index1, result.index2)
