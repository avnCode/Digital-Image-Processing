import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread("../data/lion.png")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("initial-lion",img)
img1=cv2.imread("IIScMain.png")
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
# cv2.imshow("initial-IISc",img1)

width,height=(img.shape[0],img.shape[1])
width1,height1=(img1.shape[0],img1.shape[1])
q=width*height
q1=width1*height1
p=[]
p1=[]
P=[]
P1=[]
a1=0
a11=0
z=[]
z1=[]
t1=5
t11=5
b=0
b1=0
x=0
for x in range(256):
    #ECE
    p.append((np.count_nonzero(img==x))/q)
    a1=a1+float(p[x])
    P.append(a1)
    if a1!=0 and b<2:
        b=b+1
    if b==1:
        t1=float(P[x])
    if float(P[x])==0:
        z.append(0)
    else:
        z.append(((255)*(P[x]-t1))/(1-t1))
    #IIScMain
    p1.append((np.count_nonzero(img1==x))/q1)
    a11=a11+float(p1[x])
    P1.append(a11)
    if a11!=0 and b1<2:
        b1=b1+1
    if b1==1:
        t11=float(P1[x])
    if float(P1[x]) == 0:
        z1.append(0)
    else:
        z1.append(((255)*(P1[x]-t11))/(1-t11))

i=0
j=0
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        m=img[i][j]
        img[i][j]=z[m]
i=0
j=0
for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):
        m1=img1[i][j]
        img1[i][j]=z1[m1]

cv2.imshow("Modified-lion",img)
# cv2.imshow("Modified-IISc",img1)



plt.subplot(121)
plt.title("ECE")
plt.plot(P)
plt.subplot(122)
plt.title("IIScMain")
plt.plot(P1)
plt.show()




cv2.waitKey(0)
