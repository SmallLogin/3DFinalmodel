import numpy
import math
# xy_coordinate = []
# 转换后的XY坐标集
def millerToXY (lon, lat):
    xy_coordinate = []
    L = 6381372*math.pi*2
    W = L
    H = L/2
    mill = 2.3
    x = lon*math.pi/180
    y = lat*math.pi/180
    y = 1.25*math.log(math.tan(0.25*math.pi+0.4*y))
    x = (W/2)+(W/(2*math.pi))*x
    y = (H/2)-(H/(2*mill))*y
    xy_coordinate.append([round(y), round(x)])
    return xy_coordinate

g1=[45.5348,-122.6940]
g1xy = [6382510, 6300140]
g2=[45.5348,-122.6876]
g2xy = [6383223, 6300140]
g3=[45.5302,-122.6940]
g3xy = [6382510, 6300575]
g4=[45.5302,-122.6876]
g4xy = [6383223, 6300575]

g5 = [45.53186892, -122.68891042 ]

lon = g5[1]
lat = g5[0]
xy = millerToXY(lon,lat)

print(xy)