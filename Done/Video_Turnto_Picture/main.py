import cv2

'''
Input:  Video_path(视频路径)
        Picture_gap(每多少帧取一张图片)
'''
def video_Turnto_picture(Video_path, Picture_gap):
    cap = cv2.VideoCapture(Video_path)
    sucess_flag = cap.isOpened()    #判断图片读取是否成功 成功返回True
    frame_count = 0     #记录帧数
    Picture_Number = 0       #用与图片命名序号
    while sucess_flag:
        frame_count += 1
        sucess_flag, frame = cap.read()     #按帧读取视频，返回值ret是布尔型，正确读取则返回True，frame为每一帧的图像
        if sucess_flag:
            if (frame_count % Picture_gap == 0):      #判断间隔多少张保存图片
                out_path = Picture_Path + '/hi%d' %Picture_Number + '.jpg'
                cv2.imwrite(out_path, frame)
                Picture_Number += 1
    cap.release()       #释放内存

if __name__ == '__main__':
    Video_Path = 'D:/project/Python/PDL_Python/Video_Turnto_Picture/我从未见过如此究极沙雕的视频.mp4'
    Picture_Path = 'D:/project/Python/PDL_Python/Video_Turnto_Picture/123'
    video_Turnto_picture(Video_Path, 1)
