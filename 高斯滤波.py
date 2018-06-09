import cv2

img = cv2.imread("test.jpg", cv2.IMREAD_UNCHANGED)
blurred_img = cv2.GaussianBlur(img, (15, 15), 0)    # 核大小必须是奇数 核越大 滤波效果越强
gauss_img = img - blurred_img
cv2.imshow("gauss_img", gauss_img)
cv2.waitKey()