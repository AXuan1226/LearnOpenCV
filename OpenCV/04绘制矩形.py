# 导入cv模块
import cv2
# 读取图片
img = cv2.imread("1.jpg")

# 坐标
x,y,w,h=100,100,100,100
# 绘制矩形
cv2.rectangle(img,(x,y,x+w,y+h),color=(0,0,0),thickness=1)      # 参数说明：(图片，显示坐标，颜色=(RGB)，宽度)
# 绘制圆形
cv2.circle(img,center=(x+w,y+h),radius=100,color=(255,0,0),thickness=2)   # 参数说明：(图片，圆心坐标，半径，颜色=(RGB)，宽度)
# 显示
cv2.imshow('re_img',img)
# 等待
# 按下Q退出
while True:
    if ord('q') == cv2.waitKey(0):
        break
# 释放内存
cv2.destroyAllWindows()