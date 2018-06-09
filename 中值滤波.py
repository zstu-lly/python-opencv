import cv2

img = cv2.imread("xiebiao.png", cv2.IMREAD_UNCHANGED)
result_img = cv2.medianBlur(img, 3)    # 核的大小必须是奇数
cv2.imshow("img", img)
cv2.imshow("result_img", result_img)
cv2.waitKey()