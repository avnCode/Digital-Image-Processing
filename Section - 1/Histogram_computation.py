import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread('../data/GulmoharMarg.png')
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img2=cv2.imread('../data/GulmoharMargBright.png')
imgray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

img3=cv2.imread('../data/GulmoharMargDark.png')
imgray3=cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)


i=0
x=[]
y=[]
z=[]
for i in range(256):
	x.append(np.count_nonzero(imgray==i))	#appending Frequency of occurence of Intensities in first Image
	y.append(np.count_nonzero(imgray2==i))
	z.append(np.count_nonzero(imgray3==i))

#GulmoharMarg
plt.subplot(321)
plt.title("GulmoharMarg(Self)")
plt.plot(x, color="Red")
plt.subplot(322)
plt.title("GulmoharMarg(In-Build)")
plt.hist(imgray.ravel(), bins=256, range=(0, 255))


#GulmoharMargDark
plt.subplot(323)
plt.title("GulmoharMargDark(Self)")
plt.plot(z, color="Black")
plt.subplot(324)
plt.title("GulmoharMargDark(In-Build)")
plt.hist(imgray3.ravel(), bins=256, range=(0, 255))

#GulmoharMargBright
plt.subplot(325)
plt.title("GulmoharMargBright(Self)")
plt.plot(y, color="Red")
plt.subplot(326)
plt.title("GulmoharMargBright(In-Build)")
plt.hist(imgray2.ravel(), bins=256, range=(0, 255))
plt.show()


