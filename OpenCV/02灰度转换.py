# 导入cv模块
import cv2

# 读取图片
img = cv2.imread("1.jpg")
# 灰度转换
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 显示灰度
cv2.imwrite('gray_img.jpg', gray_img)
# 显示图片
cv2.imshow("1", img)
# 等待
cv2.waitKey(0)
# 释放内存
cv2.destroyAllWindows()
