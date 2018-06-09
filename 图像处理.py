# coding: utf-8
import cv2
img = cv2.imread("test.jpg", cv2.IMREAD_UNCHANGED)
# BGR图像
print(img[100, 100])
img[100, 100] = [255, 255, 255]
print(img[100, 100])
cv2.imshow("original", img)
img[100: 150, 100: 150] = [0, 0, 0]
cv2.imshow("result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
