import numpy as np
import matplotlib.pyplot as plt
import cv2

img=cv2.imread('../data/coins.png')
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

h=cv2.calcHist([imgray],[0],None,[256],[0,256])
inter=[]
intra=[]


for i in range(1,257):
	x,y=np.split(h,[i])
	x=x/(imgray.shape[0]*imgray.shape[1]) # normalize HISTOGRAM
	y=y/(imgray.shape[0]*imgray.shape[1]) # normalize HISTOGRAM

#finding class prob
	w1= np.sum(x) #Class Prob
	w2=np.sum(y) #Class Prob

#finding class mean and class variance
	if w1==0:
		sum1=0 #Case when division by w1 : NaN sum=X/0
	else:
		sum1=[x[j]*j for j in range(len(x))]/w1  #Class Mean 1
	if w2==0:
		sum2=0 ##Case when division by w2 : NaN sum=X/0
	else:
		sum2=[y[j]*(j+i) for j in range(len(y))]/w2 #Class Mean 2
	
	if w1==0:
		u1=0
		sd1=0
	else:
		u1=np.sum(sum1) #Used for calc Class Variance & Inter class Variance
		s1=[(j-u1)**2*x[j] for j in range(len(x))] #Class Variance
		sd1=np.sum(s1)

	
	if w2==0:
		u2=0
		sd2=0
	else:
		u2=np.sum(sum2) #Used for calc Class Variance & Inter class Variance
		s2=[(j+i-u2)**2*y[j] for j in range(len(y))] #Class Variance
		sd2=np.sum(s2)
	
	
	intra.append((w1*(sd1**2)+w2*(sd2**2))) #Intra class Variance for every Intensity Threshold
	inter.append((w1*w2)*((u1-u2)**2))
total=intra+inter
ans1=intra.index(min(intra))
ans2=inter.index(max(inter))
print('Min of Within Class Variance',ans1)
print('Max of Between Class Variance',ans2)


plt.subplot(131)
plt.title('Within Class Variance')
plt.plot(intra)
plt.subplot(132)
plt.title('Between Class Variance')
plt.plot(inter)
plt.subplot(133)
plt.title('TOTAL')
plt.plot(total)
plt.show()	



(thres,bin)=cv2.threshold(imgray,ans1,255,cv2.THRESH_BINARY)
cv2.imshow('Binarized Image by Within Class Variance ',bin)

(thres,bin)=cv2.threshold(imgray,ans2,255,cv2.THRESH_BINARY)
cv2.imshow('Binarized Image by Between Class Variance ',bin)

cv2.waitKey(0)
