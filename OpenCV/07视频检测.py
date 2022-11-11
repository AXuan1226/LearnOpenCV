# 导入cv模块
import cv2
import numpy


# 检测函数
def face_detect_demo(img):
    gray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # 第一步进行灰度转换
    # 加载一个分类器，opencv已经训练好的人脸识别分类器
    # 下面就是调用openCV的一个识别面部的分类器
    face_detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # face_detect.detectMultiScale的参数说明：(放入的图像，缩放倍数，确定次数也就是要检测多少次才能确定有这个人脸，默认0，人脸最大是多大也就是一张图片上的人脸大概都是多大，就给限制一下)
    face = face_detect.detectMultiScale(gray,1.01)
    # 检测图像绘制一个框
    for x,y,w,h in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=1)
    cv2.imshow('result',img)
# 读取摄像头
# cap = cv2.VideoCapture(0)    # 默认0为本机摄像头，其他数字为外接其他摄像头
# 读取视频文件
cap = cv2.VideoCapture('face.mp4')
# 等待
# 按下Q退出
while True:
    # 如果摄像头有图像则返回一个True
    flag,frame = cap.read()
    if not flag:
        break
    face_detect_demo(frame)
    if ord(' ') == cv2.waitKey(1):
        break
# 释放内存
cv2.destroyAllWindows()
# 释放摄像头
cap.release