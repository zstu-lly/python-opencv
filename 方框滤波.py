import cv2

img = cv2.imread("test.jpg", cv2.IMREAD_UNCHANGED)
# 处理结果 = cv2.boxFilter(原始图像, 目标图像深度(-1表示与原始图像一致), 核大小,
#                          normalize=True表示进行均值滤波 False表示对核范围内的灰度值求和 很容易发生溢出超过255)
result_img = cv2.boxFilter(img, -1, (1, 1), normalize=False)
cv2.imshow("result_img", result_img)
cv2.waitKey()