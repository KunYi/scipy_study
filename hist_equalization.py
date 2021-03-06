#!/usr/bin/python

import numpy as np
from scipy import misc as mc
import matplotlib.pyplot as plt

def getHist(img):
	h = np.zeros(256)
	for i in img.flatten():
		h[i] = h[i] + 1
	return h

def normalizeiHist(h, t):
	for i in range(256):
		h[i] = h[i]/t
	return h

def getCDF(h):
	cdf = np.zeros(256)
	cdf[0] = h[0]
	for i in range(1,256):
		cdf[i] = cdf[i-1] + h[i]
	return cdf

	
lena = mc.lena()
# to get image height & witdh
x, y = lena.shape
# get total pixel
t = x*y

f, axarr = plt.subplots(2,3)
plt.gray()
axarr[0, 0].imshow(lena)
axarr[0, 0].set_title('original image')

hist = getHist(lena)
hist = normalizeiHist(hist, t)
ylim_max = hist.max() * 1.05
axarr[0, 1].bar(range(256), hist)
axarr[0, 1].set_xlim([0,255])
axarr[0, 1].set_ylim([0,ylim_max])
axarr[0, 1].set_title('histogram')

cdp = getCDF(hist)

axarr[0, 2].plot(np.linspace(0,1,256),cdp)
axarr[0, 2].set_title('CDF')

# histogram equalization
nlena = np.zeros([x,y], dtype=np.uint8)
for i in range(x):
	for j in range(y):
		t = cdp[lena[i,j]]*255
		nlena[i,j]=t

axarr[1, 0].imshow(nlena)
axarr[1, 0].set_title('After equlazation')

# re-calc new lena
x, y = nlena.shape
t = x*y
hist = getHist(nlena)
hist = normalizeiHist(hist, t)

axarr[1, 1].bar(range(256), hist)
axarr[1, 1].set_xlim([0,255])
axarr[1, 1].set_ylim([0,ylim_max])

cdf = getCDF(hist)
axarr[1, 2].plot(np.linspace(0,1,256),cdf)

plt.show()


