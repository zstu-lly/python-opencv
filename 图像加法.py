import cv2
import numpy as np

img = cv2.imread("test.jpg", cv2.IMREAD_UNCHANGED)
img_bak = img           # 像素和 = 像素和 % 255
add_1 = img + img_bak    # 当像素值和 > 255 时直接取255
add_2 = cv2.add(img, img_bak)
cv2.imshow("add_1", add_1)
cv2.imshow("add_2", add_2)
cv2.waitKey(0)
cv2.destroyAllWindows()