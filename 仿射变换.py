import cv2
import numpy as np

# 读取一张斯里兰卡拍摄的大象照片
img = cv2.imread('lena.jpg')

# 沿着横纵轴放大1.6倍，然后平移(-150,-240)，最后沿原图大小截取，等效于裁剪并放大
param1 = np.array([[1.6, 0, -150],[0, 1.6, -240]], dtype=np.float32)
img_new1=cv2.warpAffine(img,param1,(512,512))
cv2.imwrite('lena1.jpg', img_new1)

# x轴的剪切变换,15度
theta = 15* np.pi/180
param2 = np.array([[1, np.tan(theta), 0],[0, 1, 0]], dtype=np.float32)
img_new2= cv2.warpAffine(img,param2,(512,512))
cv2.imwrite('lena2.jpg',img_new2)

# 顺时针旋转15度
param3=np.array([[np.cos(theta),-np.sin(theta),0],[np.sin(theta),np.cos(theta),0]],dtype=np.float32)
img_new3=cv2.warpAffine(img,param3,(512,512))
cv2.imwrite('lena3.jpg',img_new3)

# 某种变换，具体旋转+缩放+旋转组合可以通过SVD分解理解
M = np.array([[1, 1.5, -400],[0.5, 2, -100]], dtype=np.float32)
img_new4 = cv2.warpAffine(img, M, (512,512))
cv2.imwrite('lena4.jpg', img_new4)


# cv2.namedWindow('new_window', cv2.WINDOW_NORMAL)
# cv2.imshow('new_window',img_new1)
# cv2.imshow('lena_new1',img)
# cv2.waitKey()
