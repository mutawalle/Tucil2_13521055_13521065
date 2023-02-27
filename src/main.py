from type import Point, TwoPointDistance
from ioProcedure import inputProc, printResPoint
from algorithm import minimumTwoPointDistance, bruteForce
import algorithm

# plotting
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# time
import time

# platform
import platform

n: int = 0
d: int = 0
listPoint: list[Point] = []
result: TwoPointDistance

print("============================================")
print("====            CLOSEST POINT            ===")
print("============================================")
print()

# Input banyak point (n) dan dimensi (d)
inputProc(n, d, listPoint)

if (listPoint[0].dimension < 2 or len(listPoint) < 2):
    print("Maaf, program hanya bisa menghitung point dengan dimensi > 1 dan titik > 1")
else:
    print()
    print("--- System Specs ---")
    my_system = platform.uname()
    print(f"System       : {my_system.system}")
    print(f"Node Name    : {my_system.node}")
    print(f"Release      : {my_system.release}")
    print(f"Version      : {my_system.version}")
    print(f"Machine      : {my_system.machine}")
    print(f"Processor    : {my_system.processor}")
    print()

    start_time = time.time()
    result, resultList = minimumTwoPointDistance(listPoint)
    res_time = time.time() - start_time
    print("--- Divide & Conquer Algorithm ---")
    print("Execution time: %s seconds" % (res_time))
    print("Count amount: ", algorithm.countDNC)
    print("Jarak terpendek yang didapat: ", result.distance, " satuan")

    printResPoint(resultList, result.index1)
    printResPoint(resultList, result.index2)
    print()

    start_time = time.time()
    resultBF = bruteForce(listPoint)
    res_time = time.time() - start_time
    print("--- Brute Force Algorithm ---")
    print("Execution time: %s seconds" % (res_time))
    print("Count amount: ", algorithm.countBF)
    print("Jarak terpendek yang didapat: ", resultBF.distance, " satuan")

    printResPoint(listPoint, resultBF.index1)
    printResPoint(listPoint, resultBF.index2)
    print()

    if (listPoint[0].dimension == 3):
        fig = plt.figure()
        ax = plt.axes(projection='3d')

        x_values = []
        y_values = []
        z_values = []

        for i in range(len(resultList)):
            if (i == result.index1 or i == result.index2):
                xdata = resultList[i].values[0]
                x_values.append(xdata)

                ydata = resultList[i].values[1]
                y_values.append(ydata)

                zdata = resultList[i].values[2]
                z_values.append(zdata)

                ax.scatter3D(xdata, ydata, zdata, color = "red")
            else:
                xdata = resultList[i].values[0]
                ydata = resultList[i].values[1]
                zdata = resultList[i].values[2]

                ax.scatter3D(xdata, ydata, zdata, color = "blue")

        ax.plot(x_values, y_values, z_values, color = "red")
        ax.set_title('3D Points', fontsize = 14)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')

        plt.show()
    elif (listPoint[0].dimension == 2):
        fig = plt.figure()

        x_values = []
        y_values = []

        for i in range(len(resultList)):
            if (i == result.index1 or i == result.index2):
                xdata = resultList[i].values[0]
                x_values.append(xdata)
                ydata = resultList[i].values[1]
                y_values.append(ydata)
                plt.scatter(xdata, ydata, color = "red")
            else:
                xdata = resultList[i].values[0]
                ydata = resultList[i].values[1]
                plt.scatter(xdata, ydata, color = "blue")
        
        plt.plot(x_values, y_values, color = "red")
        plt.title('2D Points', fontsize = 14)
        plt.xlabel('x')
        plt.ylabel('y')

        plt.show()


