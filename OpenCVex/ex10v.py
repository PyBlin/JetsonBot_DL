from OpenCV_Functions import *

def imageProcessing(image):
    image = imageCopy(image)
    image_gray = convertColor(image, cv2.COLOR_BGR2GRAY)
    # image_edge = cannyEdge(image_gray, 100, 200)
    height, width = image.shape[:2]

    # warp perspective
    pt1 = [int(width*0.45), int(height*0.65)]
    pt2 = [int(width*0.55), int(height*0.65)]
    pt3 = [width, height*1.0]
    pt4 = [0, height*1.0]
    roi_corners = np.array([[pt1, pt2, pt3, pt4]], dtype=np.int32)
    result = polyROI(image, roi_corners)

    result = cannyEdge(image_gray, 100, 200)
    lines = houghLinesP(result, 1, np.pi/180, 40)

    # lx, ly, rx, ry = 
    result = lineFitting(image, lines, (0, 0, 255), 5, 5. * np.pi / 180.)
    return result



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
