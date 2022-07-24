import cv2
from PIL import Image

def opencvImageFlip():
    image = cv2.imread("C:\\Users\\erics\\OneDrive\\Desktop\\videoFrames\\rickrollframe1.jpg")
    image = cv2.rotate(image,cv2.ROTATE_180)
    cv2.imshow("Flipping Image :( | ):",image)
    cv2.waitKey(0)

def pillowImageFlip():
    image = Image.open("C:\\Users\\erics\\OneDrive\\Desktop\\videoFrames\\rickrollframe1.jpg")
    image = image.rotate(180,expand=True)#expand not really needed but I'm writing it to practice
    image.show()


pillowImageFlip()
opencvImageFlip()
