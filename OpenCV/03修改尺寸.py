# 导入cv模块
import cv2
# 读取图片
img = cv2.imread("1.jpg")
# 修改尺寸
resize_img = cv2.resize(img, dsize=(200, 200))      # 修改大小为200*200dp
#显示图片
cv2.imshow("1", img)
# 显示修改后的
cv2.imshow('resize_img',resize_img)
# 打印图尺寸大小
print('未修改的',img.shape)
print('修改后的',resize_img.shape)

# 等待
# 按下Q退出
while True:
    if ord('q') == cv2.waitKey(0):
        break
# 释放内存
cv2.destroyAllWindows()