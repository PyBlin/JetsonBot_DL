from OpenCV_Functions import *

def imageProcessing(image):
    result = imageCopy(image)

    lower_white_hls = np.array([0, 200, 0])
    upper_white_hls = np.array([179, 255, 255])
    lower_yellow_hls = np.array([15, 30, 115])
    upper_yellow_hls = np.array([35, 204, 255])

    result = convertColor(result, cv2.COLOR_BGR2HLS)
    white_hls_overlay = splitColor(result, lower_white_hls, upper_white_hls)
    yellow_hls_overlay = splitColor(result, lower_yellow_hls, upper_yellow_hls)
    result = white_hls_overlay + yellow_hls_overlay
    
    result = convertColor(result, cv2.COLOR_HLS2BGR)
    return result

imagePath = "./solidWhiteCurve.jpg"
image = imageRead(imagePath)
imageShow("Opened Image", image)

result = imageProcessing(image)

imageShow("image", result)

cv2.destroyAllWindows()
