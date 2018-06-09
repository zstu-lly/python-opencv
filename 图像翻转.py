import cv2

img = cv2.imread("test.jpg", cv2.IMREAD_UNCHANGED)
dst = cv2.flip(img, flipCode=0)    # flipCode = 0 代表上下翻转
cv2.imshow("dst", dst)
dst = cv2.flip(img, 1)    # flipCode > 0 代表左右翻转
cv2.imshow("dst_", dst)
dst = cv2.flip(img, -1)    # flipCode < 0 代表左右翻转一次 上下翻转一次
cv2.imshow("dst__", dst)
cv2.waitKey()
