# 导入cv模块
import cv2
import numpy


# 检测函数
def face_detect_demo():
    gray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # 第一步进行灰度转换
    # 加载一个分类器，opencv已经训练好的人脸识别分类器
    # 下面就是调用openCV的一个识别面部的分类器
    face_detect = cv2.CascadeClassifier('C:/Users/axuan/Documents/python/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')
    # face_detect.detectMultiScale的参数说明：(放入的图像，缩放倍数，确定次数也就是要检测多少次才能确定有这个人脸，默认0，人脸最大是多大也就是一张图片上的人脸大概都是多大，就给限制一下)
    face = face_detect.detectMultiScale(gray,1.01)
    # 检测图像绘制一个框
    for x,y,w,h in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=1)
    cv2.imshow('result',img)
# 读取图片
img = cv2.imread("face2.jpg")
img = numpy.array(img)
# 调用检测函数
face_detect_demo()
# 等待
# 按下Q退出
while True:
    if ord('q') == cv2.waitKey(0):
        break
# 释放内存
cv2.destroyAllWindows()