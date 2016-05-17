#!/usr/bin/python
 
#----------------------------------------------------------------------
# Author: Roberto Pasillas
#----------------------------------------------------------------------
# Description: This program a file name passed in through command line
#   argumement to calculate the distance of the closest pair.
#----------------------------------------------------------------------

import sys


class Point:
    def __init__(self, x_val, y_val):
        self.x = x_val
        self.y = y_val

    def __repr__(self):
        return "(%.2f, %.2f)" % (self.x, self.y)


def Read_Points_From_Command_Line_File():
    points = []
    number_of_args = len(sys.argv)
    file = open(sys.argv[1], "r")

    for line in file:
        line.strip()
        x_y = line.split(" ")
        points.append(Point(float(x_y[0]), float(x_y[1])))

    return points


def Write_to_File(filename, s):
    output = open(filename, 'w')
    output.write(str(s))
    output.write('\n')


def Distance(Point1, Point2):
    x = (Point1.x - Point2.x) ** 2
    y = (Point1.y - Point2.y) ** 2
    r = (x + y) ** .5
    return r


def BruteForce(s):
    minV = float("inf")
    for i, P1 in enumerate(s):
        for P2 in s[i + 1:]:
            temp = Distance(P1, P2)
            if minV > temp:
                minV = temp
    return minV


def DivideConquer(s, sY):
    if len(s) < 2:
        return float("inf")
    elif len(s) == 2:
        return Distance(s[0],s[1])
    else:
        mid = len(s) / 2
        yL, yR = splitX(sY, s[mid])
        minL = DivideConquer(s[:mid], yL)
        minR = DivideConquer(s[mid:], yR)
        return merge(s, sY, mid, min(minL, minR))

def splitX(list, pivot):
    listL, listR = [], []
    for point in list:
        if point.x < pivot.x:
            listL.append(point)
        else:
            listR.append(point)
    return listL, listR

def merge(s, sY, mid, d):
    minV = d

    sYFiltered = filter(lambda p: abs(p.x - s[mid].x) <= d, sY)

    for i ,p1 in enumerate(sYFiltered):
        for p2 in sYFiltered[i + 1:min(i + 5, len(sYFiltered))]:
            if abs(p2.y - p1.y) > d:
                break
            temp = Distance(p1, p2)
            if minV > temp:
                minV = d = temp
    return minV


def main():
    list = Read_Points_From_Command_Line_File()
    prename = sys.argv[1].split(".")
    if len(sys.argv) == 3 and sys.argv[2] == "-B":
        Write_to_File(prename[0]+"_distance.txt",BruteForce(list))
    else:
        listX = sorted(list, key=lambda Point: Point.x)
        listY = sorted(list, key=lambda Point: Point.y)
        Write_to_File(prename[0]+"_distance.txt",DivideConquer(listX, listY))


main()
