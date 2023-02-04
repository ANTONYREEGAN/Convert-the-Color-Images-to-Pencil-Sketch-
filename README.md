# Convert-the-Color-Images-to-Pencil-Sketch-






#### import numpy as np
#### import imageio
#### import cv2
#### import scipy.ndimage
#These are the Libraries needed for this program

#### img = "3861505.jpg"
#### def rgb2gray(rgp):
   #### return np.dot(rgp[...,:3],[0.2989,0.5870,0.1140]) # It is the 2 dimensional array formula to convert image to gray scale
    
#### def dodge(front,back):
   #### finalsketch =  front*255/(255-back) # If the iamge scale is greater than 255 it will convert it back to 255
   #### finalsketch[finalsketch>255]=255
   #### finalsketch[back == 255]=255
   #### return finalsketch.astype('uint8') # To convert any suitable existing colounm to categorical type we will use aspect function and uint8 is for 8 - bit signed int 

#### ss = imageio.imread(img) # to read the image
#### gray = rgb2gray(ss) #  The image is converted gray scale
#### i = 255-gray
#### blur = scipy.ndimage.filters.gaussian_filter(i,sigma = 15)
#### r = dodge(blur,gray)
#### cv2.imwrite("3861505.jpg",r) # this function will convert the image to sketch by taking two parameters as blur and gray
