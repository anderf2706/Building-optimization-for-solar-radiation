import rhinoscriptsyntax as rs
import Rhino.Geometry as geo
import math
import random


def createBox(length, width, height, point):
    a = geo.Point3d(point[0], point[1], point[2])
    b = geo.Point3d(point[0] + length, point[1], point[2])
    c = geo.Point3d(point[0] + length, point[1] + width, point[2])
    d = geo.Point3d(point[0], point[1] + width, point[2])
    e = geo.Point3d(point[0], point[1], point[2] + height)
    f = geo.Point3d(point[0] + length, point[1], point[2] + height)
    g = geo.Point3d(point[0] + length, point[1] + width, point[2] + height)
    h = geo.Point3d(point[0], point[1] + width, point[2] + height)

    points = []
    points.append(a)
    points.append(b)
    points.append(c)
    points.append(d)
    points.append(e)
    points.append(f)
    points.append(g)
    points.append(h)

    rs.AddBox(points)


# createBox(2,1,1,[0,0,0])


def generateRandom(maxheight, maxlength, maxCubes):
    print("generating")
    maxXlength = 50
    maxYlength = 50
    minsize = 3
    for i in range(maxCubes):
        height = random.randint(minsize, maxheight)
        width = random.randint(minsize, maxlength)
        length = random.randint(minsize, maxlength)
        xpos = random.randint(0, maxXlength)
        ypos = random.randint(0, maxYlength)
        createBox(length, width, height, [xpos, ypos, 0])


def createSideWaysCube(point1, point2, point3, point4, height):
    a = geo.Point3d(point1[0], point1[1], 0)
    b = geo.Point3d(point2[0], point2[1], 0)
    c = geo.Point3d(point3[0], point3[1], 0)
    d = geo.Point3d(point4[0], point4[1], 0)
    e = geo.Point3d(point1[0], point1[1], height)
    f = geo.Point3d(point2[0], point2[1], height)
    g = geo.Point3d(point3[0], point3[1], height)
    h = geo.Point3d(point4[0], point4[1], height)

    points = []
    points.append(a)
    points.append(b)
    points.append(c)
    points.append(d)
    points.append(e)
    points.append(f)
    points.append(g)
    points.append(h)

    rs.AddBox(points)


def createMultiple():
    for i in range(10):
        for j in range(10):
            for k in range(10):
                createBox(1, 1, 1, [i * 2, j * 2, k * 2])


# createMultiple()


def createRandomBOxes():
    for i in range(1000):
        x = random.randint(-50, 50)
        y = random.randint(-50, 50)
        z = random.randint(0, 100)
        height = random.randint(1, 10)
        weight = random.randint(1, 10)
        length = random.randint(1, 10)
        createBox(height, weight, length, [x, y, z])


# createRandomBOxes()
# createBox(2,5,3,[10,0,0])


def generateRandomstructure():
    createBox(10, 40, 30, [-50, -50, 0])
    createBox(10, 30, 20, [-50, -10, 0])
    createSideWaysCube([-50, 20], [-40, 20], [0, 50], [0, 60], 20)


if (x):
    generateRandom(20, 10, 10)
    # generateRandomstructure()

    # createBox(length,width, height, point):

    # createBox(5, 5, 5, [0,0,0])

    # createBox(10, 10, 10, [1,1,1])