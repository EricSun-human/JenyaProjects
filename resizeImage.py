import cv2
from PIL import Image

def opencvResize():
    img = cv2.imread('C:\\Users\\erics\\OneDrive\\Desktop\\videoFrames\\rickrollframe1.jpg', cv2.IMREAD_UNCHANGED)
    width = int(img.shape[1] * 0.5)
    height = int(img.shape[0] * 0.5)  
    # resize image
    resizedImg = cv2.resize(img, [width,height])
    print('Original Dimensions : ',img.shape)
    print('Resized Dimensions : ',resizedImg.shape)
    cv2.imshow("Resized image", resizedImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def pillowResize():
    img = Image.open('C:\\Users\\erics\\OneDrive\\Desktop\\videoFrames\\rickrollframe1.jpg')
    print('Original Dimensions : '+str(img.size))
    width=int(img.size[0]*0.5)
    height= int(img.size[1]*0.5)

    resizedImg = img.resize((width,height))
    resizedImg.show()
#opencvResize()
pillowResize()