'''Connected Component analysis to count number of shapes in an image
'''
import cv2
import numpy as np

img=cv2.imread('../data/Shapes.png')
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

th=0
thres,Bin=cv2.threshold(imgray,th,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
Bin=(Bin/255) #Normalize Intensity levels
height, width = Bin.shape
#Counting Number of Shapes

# c=0
#Region Counter
k=0
c=-1
R=np.zeros(Bin.shape) #New Region
trash=[] #Repeat Region List
for i in range(height):
	for j in range(width):
		if Bin[i][j]==0:
			k=k+0
		elif Bin[i][j]==1 and Bin[i][j-1]==0 and Bin[i-1][j]==0:
			R[i][j]=k
			k=k+1 #region counter increment
			c=c+1
		elif Bin[i][j]==1 and Bin[i-1][j]==1 and Bin[i][j-1]==0:
			R[i][j]=R[i-1][j]
		elif Bin[i][j]==1 and Bin[i-1][j]==0 and Bin[i][j-1]==1:
			R[i][j]=R[i][j-1]
		elif Bin[i][j]==1 and Bin[i-1][j]==1 and Bin[i][j-1]==1:
			R[i][j]=R[i-1][j]

		if R[i-1][j] != 0 and R[i][j-1]!=0 and R[i-1][j]!=R[i][j-1] and trash.count([R[i-1][j], R[i][j-1]]) == 0:
			c=c-1
			trash.append([R[i-1][j], R[i][j-1]])
			trash.append([R[i][j-1], R[i-1][j]])
			D=R #Creating Copy of New Region to Directly Change the connected region to one number
			x = D[i][j-1]
			D[np.where(D == x)] = D[i - 1][j]
#Counting Circles
l=0
for i in range(k+1):
	if np.count_nonzero(D==i) in range (150,600):
		l=l+1

print('Number of Shapes:',c)
print('Number of Circles:',l)


cv2.waitKey(0)
