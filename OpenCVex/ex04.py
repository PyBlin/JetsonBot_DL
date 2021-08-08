from OpenCV_Functions import *

imagePath = "./solidWhiteCurve.jpg"
image = imageRead(imagePath)
imageShow('image', image)

def imageProcessing(image):
	image = imageCopy(image)
	height = image.shape[0]
	width = image.shape[1]
	pt1 = (int(width * 0.35), int(height * 0.65))
	pt2 = (int(width * 0.65), int(height * 0.65))
	pt3 = (int(width), height)
	pt4 = (0, height)

	line = drawLine(image, pt1, pt2, (255, 0, 0), 3)
	line = drawLine(line, pt2, pt3, (255, 0, 0), 3)
	line = drawLine(line, pt3, pt4, (255, 0, 0), 3)
	line = drawLine(line, pt4, pt1, (255, 0, 0), 3)

	result = drawText(line, "OpenCV Video Processing", (10, 250), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (255, 0, 0), 1)
	return result

result = imageProcessing(image)
imageShow('image', result)

cv2.destroyAllWindows()
