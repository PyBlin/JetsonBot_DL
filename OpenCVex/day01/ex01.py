from OpenCV_Functions import *

def imageProcessing(image):
    result = imageCopy(image)
    for i in range(0, 200):
        for j in range(0, 200):
            image = setPixel(result, i, j, [0, 0, 0])
    return result


imagePath = "./solidWhiteCurve.jpg"
image = imageRead(imagePath)
imageShow("Opened Image", image)

result = imageProcessing(image)

imageShow("image", result)

cv2.destroyAllWindows()
