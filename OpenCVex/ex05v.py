from OpenCV_Functions import *

imagePath = "./solidWhiteCurve.jpg"
image = imageRead(imagePath) 
backup = imageCopy(image)



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

	roi_poly = np.array([[pt1, pt2, pt3, pt4]], dtype=np.int32)
	roi_active = polyROI(image, roi_poly)
	roi_deactive = image - roi_active
	# roi_active = imageMedianBlur(roi_active, 3)
	roi_active = imageGaussianBlur(roi_active, 3, 3, 3)
	# roi_deactive = imageBilateralFilter(roi_deactive, 3, 3, 3)
	roi_deactive = imageMedianBlur(roi_deactive, 3)
	image = addWeightedImage(roi_deactive, 100, roi_active, 100)

	# result = drawText(line, "OpenCV Video Processing", (10, 250), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (255, 0, 0), 1)
	return image#, result



road_video_01 = "./solidWhiteRight.mp4"
def VideoProcessing(openpath, savepath = "output.avi"):
    cap = cv2.VideoCapture(openpath)
    if cap.isOpened():
        print("Video Opened")
    else:
        print("Video Not Opened")
        print("Program Abort")
        exit()
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))
    out = cv2.VideoWriter(savepath, fourcc, fps, (width, height), True)
    cv2.namedWindow("Input", cv2.WINDOW_GUI_EXPANDED)
    cv2.namedWindow("Output", cv2.WINDOW_GUI_EXPANDED)
    import OpenCV_Functions
    while cap.isOpened():
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret:
            # Our operations on the frame come here
            output = imageProcessing(frame)
            # Write frame-by-frame
            out.write(output)
            # Display the resulting frame
            cv2.imshow("Input", frame)
            cv2.imshow("Output", output)
        else:
            break
        # waitKey(int(1000.0/fps)) for matching fps of video
        if cv2.waitKey(int(1000.0/fps)) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    return

VideoProcessing(road_video_01, "output.mp4")

