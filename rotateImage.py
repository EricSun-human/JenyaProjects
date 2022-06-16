import cv2
import imutils
from PIL import Image
import time
def opencvRotate():
    img = cv2.imread("C:\\Users\\erics\\OneDrive\\Desktop\\videoFrames\\rickrollframe1.jpg")
    img=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
    #img=imutils.rotate_bound(img,90) Question: Need to use imutils to prevent crop or not?
    cv2.imshow("Sideways img :)", img)
    cv2.waitKey(0)

def pillowRotate():
    img = Image.open("C:\\Users\\erics\\OneDrive\\Desktop\\videoFrames\\rickrollframe1.jpg")
    image = img.rotate(90,expand=True)
    image.show()

opencvRotate()
time.sleep(5)
pillowRotate()
