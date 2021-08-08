from OpenCV_Functions import *

'''
def imageRead(openpath, flag=cv2.IMREAD_UNCHANGED):
    image = cv2.imread(openpath, flag)
    if image is not None:
        print("Image Opened")
        return image
    else:
        print("Image Not Opened")
        print("Program Abort")
        exit()
def imageShow(imagename, image, flag=cv2.WINDOW_GUI_EXPANDED):
    cv2.namedWindow(imagename, flag)
    cv2.imshow(imagename, image)
    cv2.waitKey()
    return
def imageWrite(imagename, image):
    return cv2.imwrite(imagename, image)
'''

road_image_01 = "./solidWhiteCurve.jpg"

# cv2.IMREAD_COLOR
image_color = imageRead(road_image_01, cv2.IMREAD_COLOR)

# cv2.IMREAD_GRAYSCALE
image_gray = imageRead(road_image_01, cv2.IMREAD_GRAYSCALE)

# cv2.IMREAD_UNCHANGED
image_origin = imageRead(road_image_01, cv2.IMREAD_COLOR)

imageShow("image_color, cv2.WINDOW_NORMAL", image_color, cv2.WINDOW_NORMAL)
imageShow("image_color, cv2.WINDOW_AUTOSIZE", image_color, cv2.WINDOW_AUTOSIZE)
imageShow("image_color, cv2.WINDOW_FREERATIO", image_color, cv2.WINDOW_FREERATIO)
imageWrite("gray.jpg", image_gray)
