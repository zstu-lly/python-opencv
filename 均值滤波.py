import cv2

img = cv2.imread("test.jpg", cv2.IMREAD_UNCHANGED)
result_img = cv2.blur(img, (5, 5))    # 对周围5*5范围内的像素点取均值
cv2.imshow("img", img)
cv2.imshow("result_img", result_img)
cv2.waitKey()
