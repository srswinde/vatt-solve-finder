import numpy as np
from PIL import Image
import cv2
from time import sleep
from matplotlib import pyplot as plt
cap=cv2.VideoCapture("http://vatt.as.arizona.edu:42080/axis-cgi/mjpg/video.cgi?resolution=CIF&camera=3")


b,im1=cap.read()
sleep(2.0)
b,im2=cap.read()


bias=im2-im1


plt.imshow(bias)
