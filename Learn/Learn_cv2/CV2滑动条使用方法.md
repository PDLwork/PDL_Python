函数 cv2.createTrackbar()
cv2.createTrackbar(“scale”, “display”, 0, 100, self.opencv_calibration_node.on_scale)
1
功能
绑定滑动条和窗口，定义滚动条的数值

参数
第一个参数时滑动条的名字，
第二个参数是滑动条被放置的窗口的名字，
第三个参数是滑动条默认值，
第四个参数时滑动条的最大值，
第五个参数时回调函数，每次滑动都会调用回调函数。
函数 cv2.getTrackbarPos()：
cv2.getTrackbarPos("hue min", "TrackBars")
1
功能
得到滑动条的数值

参数
第一个参数是滑动条名字，
第二个时所在窗口，
返回值是滑动条的数值
函数 cv2.setTrackbarPos()
cv2.setTrackbarPos(‘Alpha’, ‘image’, 100)
1
功能
设置滑动条的默认值

参数
第一个参数是滑动条名字，
第二个时所在窗口，
第三个参数是滑动条默认值，
————————————————
版权声明：本文为CSDN博主「唐僧洗头用飘柔dp」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_45860565/article/details/119117899