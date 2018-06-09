import cv2
img = cv2.imread("test.jpg", cv2.IMREAD_UNCHANGED)

region = img[100: 200, 100: 200]    # 将一个区域的图像复制到另一个区域
img[200: 300, 200: 300] = region
cv2.imshow("result", img)
cv2.waitKey(0)
