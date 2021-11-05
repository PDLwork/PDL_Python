import cv2

def video_pic(path):
    cap = cv2.VideoCapture(path)
    sucess = cap.isOpened()
    frame_count = 0
    i = 0
    while sucess:
        frame_count += 1
        sucess, frame = cap.read()
        if (frame_count % 3 == 0):
            i += 1
            cv2.imwrite('D:/project/Python/PDL_Python/Video_Turnto_Photo/123/s%d.jpg' % i, frame)
    cap.release()

if __name__ == '__main__':
    path = "D:/project/Python/PDL_Python/Video_Turnto_Photo/我从未见过如此究极沙雕的视频.mp4"
    video_pic(path)
