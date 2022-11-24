import cv2
import numpy as np

###Otsu
img1=cv2.imread('../data/DoubleColorShapes.png')
imgray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

th=0
thres,Bin5=cv2.threshold(imgray1,th,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
Bin5=1-(Bin5/255) #Inverting Image to standard calculation
cv2.imshow('Otsu binarized image',Bin5)
###

###MSER
img=cv2.imread('../data/DoubleColorShapes.png')
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow('Original gray image + Otsu',imgray)
th=0
thres,Bin=cv2.threshold(imgray,th,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
Bin1=255-Bin #Finding Objects by threshold
Bin=imgray+Bin1 #adding both objects detected by threshold and gray scale for easier calculation

th=0
thres,Bin=cv2.threshold(Bin,th,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
Bin=(Bin/255)
cv2.imshow('MSER binary image',Bin)
height, width = Bin.shape

#Counting Number of Shapes
k=0
k1=0
c=k-1
c1=k1
R=np.zeros(Bin.shape)
R1=np.zeros(Bin5.shape)
trash=[]
trash1=[]
for i in range(height):
	for j in range(width):
		if Bin[i][j]==0:
			k=k+0
		elif Bin[i][j]==1 and Bin[i][j-1]==0 and Bin[i-1][j]==0:
			R[i][j]=k
			k=k+1
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
			D=R
			x = int(D[i][j - 1])
			D[np.where(D == x)] = D[i - 1][j]

		if Bin5[i][j]==0:
			k1=k1+0
		elif Bin5[i][j]==1 and Bin5[i][j-1]==0 and Bin5[i-1][j]==0:
			R1[i][j]=k1
			k1=k1+1
			c1=c1+1
		elif Bin5[i][j]==1 and Bin5[i-1][j]==1 and Bin5[i][j-1]==0:
			R1[i][j]=R1[i-1][j]
		elif Bin5[i][j]==1 and Bin5[i-1][j]==0 and Bin5[i][j-1]==1:
			R1[i][j]=R1[i][j-1]
		elif Bin5[i][j]==1 and Bin5[i-1][j]==1 and Bin5[i][j-1]==1:
			R1[i][j]=R1[i-1][j]

		if R1[i-1][j] != 0 and R1[i][j-1]!=0 and R1[i-1][j]!=R1[i][j-1] and trash1.count([R1[i-1][j], R1[i][j-1]]) == 0:
			c1=c1-1
			trash1.append([R1[i-1][j], R1[i][j-1]])
			trash1.append([R1[i][j-1], R1[i-1][j]])
			D1=R1
			x1 = int(D1[i][j - 1])
			D1[np.where(D1 == x)] = D1[i - 1][j]
#Counting Circles
l=0
l1=0
for i in range(k+1):
	if np.count_nonzero(D==i) in range (150,600):
		l=l+1
	if np.count_nonzero(D1==i) in range (150,600):
		l1=l1+1

print('Number of Connected component detected by MSER:',c)
print('Number of Circles detected by MSER:',l)

print('Number of Connected component detected by Otsu:',c1)
print('Number of Circles detected by Otsu:',l1)


cv2.waitKey(0)
