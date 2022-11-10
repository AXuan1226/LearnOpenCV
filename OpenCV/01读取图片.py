# 导入cv模块
import cv2
# 读取图片
img = cv2.imread("face1.jpg")
#显示图片
cv2.imshow("1", img)
# 等待
cv2.waitKey(0)
# 释放内存
cv2.destroyAllWindows()