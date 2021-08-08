from OpenCV_Functions import *

def imageProcessing(image):
    result = imageCopy(image)
    lower_white_hsv = np.array([0, 200,0])
    upper_white_hsv = np.array([179, 255, 255])
    lower_yellow_hsv = np.array([15, 30, 115])
    upper_yellow_hsv = np.array([35, 204, 255])
    result = convertColor(result, cv2.COLOR_BGR2HLS)
    white_hsv_overlay = splitColor(result, lower_white_hsv, upper_white_hsv)
    yellow_hsv_overlay = splitColor(result, lower_yellow_hsv, upper_yellow_hsv)
    result = white_hsv_overlay + yellow_hsv_overlay
    result = convertColor(result, cv2.COLOR_HLS2BGR)

    return result


imagePath = "./solidWhiteCurve.jpg"
image = imageRead(imagePath)
imageShow("Opened Image", image)

result = imageProcessing(image)

imageShow("image", result)

cv2.destroyAllWindows()
