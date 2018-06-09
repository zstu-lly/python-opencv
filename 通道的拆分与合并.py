import cv2
import numpy as np

img = cv2.imread("test.jpg", cv2.IMREAD_UNCHANGED)
b, g, r = cv2.split(img)    # 返回三个通道   单独取出一个通道可以用b = cv2.split(img)[0]
rows, cols, chn = img.shape
g = np.zeros((rows, cols), img.dtype)
r = np.zeros((rows, cols), img.dtype)
merge_img = cv2.merge([b, g, r])    # 将三个通道合并
# cv2.imshow("b", b)
cv2.imshow("merge_img", merge_img)
cv2.waitKey(0)