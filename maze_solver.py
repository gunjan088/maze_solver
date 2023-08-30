
import cv2 as cv
import numpy as np
import math

img = cv.imread("C:\\Users\\jhunj\\OneDrive\\Desktop\\Task_1_Low.png")

matrix = np.array(img)
print(matrix.shape)

arrf = np.ones((100,100),int)
arrp = np.ones((100,100),tuple)
arrg = np.ones((100,100),int)

for i in range(100):
    for j in range(100):
        if(matrix[i][j][0]==113 and matrix[i][j][1]==204 and matrix[i][j][2]==45):
            print("Start Point : {} , {} ".format(i,j))
            start = (i,j)
        elif(matrix[i][j][0]==60 and matrix[i][j][1]==76 and matrix[i][j][2]==231):
            print("End Point : {} , {} ".format(i,j))
            end = (i,j)
            matrix[i][j][0]==0
        #elif(matrix[i][j][0]==255 and matrix[i][j][1]==255 and matrix[i][j][2]==255):
           # matrix[i][j][0] = 1
        elif(matrix[i][j][0]==0 and matrix[i][j][1]==0 and matrix[i][j][2]==0):
            matrix[i][j][0] = 0
        arrf[i][j] = 9999
        arrp[i][j] = -1
        arrg[i][j] = 9999

arrf[start[0]][start[1]] = 0
arrg[start[0]][start[1]] = 0
arrp[start[0]][start[1]] = 0

def dist(x):
    k = math.sqrt((x[0]-end[0])**2 + (x[1]-end[1])**2)
    return k

def unblocked(x):
    return matrix[x[0]][x[1]][0] == 0

def valid(x):
    return x[0]>=0 and x[0]<100 and x[1]>=0 and x[1]<100

openlist = []
closedlist = []
openlist.append(start)

def astar():
    while len(openlist) != 0:
        x = openlist[0]
        openlist.pop(0)
        if x in closedlist:
            continue
    
        for k in [(x[0]-1,x[1]),(x[0]+1,x[1]),(x[0],x[1]+1),(x[0],x[1]-1)]:
            if k == end:
                print("destination reached")
                arrp[k[0]][k[1]] = x
                gn = arrg[x[0]][x[1]] + 1
                arrg[k[0]][k[1]] = gn
                return 
            if valid(k) and unblocked(k):
                openlist.append(k)
                hn = dist(k)
                gn = arrg[x[0]][x[1]] + 1
                fn = hn + gn
                if arrf[k[0]][k[1]]==9999 or fn<arrf[k[0]][k[1]]:
                    arrf[k[0]][k[1]] = fn
                    arrg[k[0]][k[1]] = gn
                    arrp[k[0]][k[1]] = x
        closedlist.append(x)

a = astar()
a

destlis = []
def destlist():
    k = arrp[end[0]][end[1]] 
    while k!=start:
        destlis.append(k)
        matrix[k[0]][k[1]][0] = 255
        matrix[k[0]][k[1]][1] = 0
        matrix[k[0]][k[1]][2] = 0
        k = arrp[k[0]][k[1]]
destlist()
matrixx = np.zeros((1000,1000,3),np.uint8)

for i in range(1000):
    for j in range(1000):
        p = int(i/10)
        q = int(j/10)
        matrixx[i][j][0] = matrix[p][q][0]
        matrixx[i][j][1] = matrix[p][q][1]
        matrixx[i][j][2] = matrix[p][q][2]
        
mat = cv.resize(matrixx,(500,500))
print(arrg[end[0]][end[1]])
cv.imshow('yay',mat)
cv.waitKey(0)