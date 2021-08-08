from OpenCV_Functions import *

def imageProcessing(image):
    image = imageCopy(image)
    resultColor = convertColor(image, cv2.COLOR_BGRA2BGR)
    height, width = image.shape[:2]
    image = cannyEdge(image, 110, 270)

    # warp perspective
    src_pt1 = [int(width*0.35), int(height*0.65)]
    src_pt2 = [int(width*0.65), int(height*0.65)]
    src_pt3 = [width, height]
    src_pt4 = [0, height]
    dst_pt1 = [int(width*0.1), 0]
    dst_pt2 = [int(width*0.9), 0]
    dst_pt3 = [int(width*0.9), height]
    dst_pt4 = [int(width*0.1), height]
    src_pts = np.float32([src_pt1, src_pt2, src_pt3, src_pt4])
    dst_pts = np.float32([dst_pt1, dst_pt2, dst_pt3, dst_pt4])

    result1 = imagePerspectiveTransformation(image, src_pts, dst_pts)
    lines = houghLinesP(result1, 1, np.pi/180, 100)
    empty = np.zeros((height, width), np.uint8)
    result2 = drawHoughLinesP(empty, lines)
    result3 = imagePerspectiveTransformation(result2, dst_pts, src_pts)
    result4 = addImage(result3, resultColor)
    return result4



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
