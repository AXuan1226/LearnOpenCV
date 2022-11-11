import os

import numpy
from PIL import Image
import cv2


def getImageAndLabels(path):
# 存储人脸数据
    faceSamples=[]
# 存储姓名数据
    ids=[]
# 存储图片信息
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
# 加载分类器
    face_detector = cv2.CascadeClassifier('C:/Users/axuan/Documents/python/opencv/sources/data\haarcascades/haarcascade_frontalface_default.xml')
# 遍历列表中的图片
    for imagePath in imagePaths:
# 打开图片，灰度化，PIL有9种不同模式，1,L,P,RGB,RGBA,CMYK,YCbCr,I,F
        PIL_img=Image.open(imagePath).convert('L')
# 将图片转化为数组，以黑白深浅
        img_numpy=numpy.array(PIL_img,'uint8')
# 获取图片人脸特征
        faces = face_detector.detectMultiScale(img_numpy)
# 获取每张图片的id和姓名
        id = int(os.path.split(imagePath)[1].split('.')[0])
# 预防无面容图片
        for x,y,w,h in faces:
            ids.append(id)
            faceSamples.append(img_numpy[y:y+h,x:x+w])
# 打印脸部特征和ID
    print('id:',id)
    print('fs:',faceSamples)
    return faceSamples,ids

if __name__ == '__main__':
    # 图片路径
    path='./data/'
    # 获取图像数组和ID标签数组及姓名
    faces,ids=getImageAndLabels(path)
    # 加载识别器
    recongnizer=cv2.face.LBPHFaceRecognizer_create()
    # 训练
    recongnizer.train(faces,numpy.array(ids))
    # 保存文件
    recongnizer .write('trainer/trainer.yml')