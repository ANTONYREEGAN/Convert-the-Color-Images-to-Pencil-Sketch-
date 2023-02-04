import numpy as np
import imageio
import cv2
import scipy.ndimage

img = "3861505.jpg"
def rgb2gray(rgp):
    return np.dot(rgp[...,:3],[0.2989,0.5870,0.1140])
def dodge(front,back):
    finalsketch =  front*255/(255-back)
    finalsketch[finalsketch>255]=255
    finalsketch[back == 255]=255
    return finalsketch.astype('uint8')

ss = imageio.imread(img)
gray = rgb2gray(ss)
i = 255-gray
blur = scipy.ndimage.filters.gaussian_filter(i,sigma = 15)
r = dodge(blur,gray)
cv2.imwrite("3861505.jpg",r)