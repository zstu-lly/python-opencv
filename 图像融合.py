import cv2

# 不同图像系数不同的融合
img_a = cv2.imread("numbers.jpg")[:500, :500]
img_b = cv2.imread("alphabet.jpg")[:500, :500]    # 确保相加的两个图片大小相等
result = cv2.addWeighted(img_a, 0.5, img_b, 0.5, -100)    # 最后一个参数:亮度调节值
cv2.imshow("result", result)
cv2.waitKey(0)