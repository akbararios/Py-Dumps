import numpy as np
import cv2 as cv

# Kernel Compass Operator
Timur = np.array(([-1, 1, 1], 
                  [-1, -2, 1], 
                  [-1, 1, 1]), dtype="int")
Tenggara = np.array(([-1, -1, 1], 
                     [-1, -2, 1], 
                     [1, 1, 1]), dtype="int")
Selatan = np.array(([-1, -1, -1], 
                    [1, -2, 1], 
                    [1, 1, 1]), dtype="int")
BDaya = np.array(([1, -1, -1], 
                  [1, -2, -1], 
                  [1, 1, 1]), dtype="int")
Barat = np.array(([1, 1, -1], 
                  [1, -2, -1], 
                  [1, 1, -1]), dtype="int")
BLaut = np.array(([1, 1, 1], 
                  [1, -2, -1], 
                  [1, -1, -1]), dtype="int")
Utara = np.array(([1, 1, 1], 
                  [1, -2, 1], 
                  [-1, -1, -1]), dtype="int")
TLaut = np.array(([1, 1, 1], 
                  [1, -2, 1], 
                  [-1, -1, -1]), dtype="int")

# Fungsi Threshold
def thresholding(arrgambar,T):
    arrgambar = np.double(arrgambar)
    M = arrgambar.shape[0] # Panjang width (horizontal) dari gambar
    N = arrgambar.shape[1] # Panjang height (vertical) dari gambar
    for i in range(0,M):
        for j in range(0,N):
            if arrgambar[i,j]<T:
                arrgambar[i,j]=0
            else:
                arrgambar[i,j]=255
    return arrgambar

# Input gambar dan Melakukan Konvolusi dengan 'cv.filter2D'
image = cv.imread('img.jpg')	
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
K1 = cv.filter2D(gray, -1, Timur)
K2 = cv.filter2D(gray, -1, Tenggara)
K3 = cv.filter2D(gray, -1, Selatan)
K4 = cv.filter2D(gray, -1, BDaya)
K5 = cv.filter2D(gray, -1, Barat)
K6 = cv.filter2D(gray, -1, BLaut)
K7 = cv.filter2D(gray, -1, Utara)
K8 = cv.filter2D(gray, -1, TLaut)

# Menghitung kekuatan tepi dari gambar
KTepi = cv.max(K1,cv.max(K2,cv.max(K3,cv.max(K4,cv.max(K5,cv.max(K6,cv.max(K7,K8)))))))

# Melakukan proses thresholding pada KTepi
Tr = thresholding(KTepi,128)

# Fungsi Utama - menampilkan hasil konvolusi
cv.imshow('Figure 1 (Original)', image)
cv.waitKey(0)

cv.imshow('Figure 1 (Original)', gray)
cv.waitKey(0)

cv.imshow('Figure 2 (Tepi)', KTepi)
cv.waitKey(0)

cv.imshow('Figure 3 (Threshold)', Tr)
cv.waitKey(0)




