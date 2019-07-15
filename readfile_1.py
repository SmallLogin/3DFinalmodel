import numpy as np
import os

# a=np.loadtxt('1.txt')
# b=np.reshape(a,(10,10,10))
# print(b)
# print(type(b))
#occ_grid_name = "data/"+"occ_grid-50" + ".npy"
occ_grid_name = "occ_grid_50" + ".npy"
# np.save(file=occ_grid_known_name, arr=b)

occ_grid = np.load(file=occ_grid_name)
print(occ_grid.shape)
print(occ_grid)
#np.savetxt("occ_grid.txt",occ_grid,fmt='%d',delimiter=' ')
obstacle = 0
privacy = 0
for i in range (occ_grid.shape[0]):
    for j in range (occ_grid.shape[1]):
        for k in range (occ_grid.shape[2]):
            if occ_grid[i][j][k] == 1:
                obstacle += 1
            elif occ_grid[i][j][k] == 2 or occ_grid[i][j][k] == 3 or occ_grid[i][j][k] == 4:
                privacy += 1
obstacle_ratio = obstacle/(occ_grid.shape[0]*occ_grid.shape[1]*occ_grid.shape[2])
privacy_ratio = privacy/(occ_grid.shape[0]*occ_grid.shape[1]*occ_grid.shape[2])
print(obstacle, obstacle_ratio, privacy, privacy_ratio)