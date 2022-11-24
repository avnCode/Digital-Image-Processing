import numpy as np
import cv2
import matplotlib.pyplot as plt

a1=cv2.imread('../data/IIScText.png')
a=cv2.cvtColor(a1,cv2.COLOR_BGR2GRAY)
c=cv2.imread('../data/IIScMainBuilding.png.')

th=0
(thres,Bin)=cv2.threshold(a,th,256,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

b=a>thres
x=a1[:,:,0]
y=a1[:,:,1]
z=a1[:,:,2]
# cv2.imshow('Text2Background',c)

c[:,:,0][b]=x[b]        #change colour to BLUE
c[:,:,1][b]=y[b]	    #change colour to GREEN
c[:,:,2][b]=z[b]	    #change colour to RED

cv2.imshow('Text2Background(RED)',c)
cv2.waitKey(0)



# a.index(min(a))
