import cv2
img = cv2.imread("numbers.jpg", cv2.IMREAD_UNCHANGED)
print(img.shape)    # 图像的行数 列数 通道数
print(img.size)    # 图像的像素数目: 行数 * 列数 * 通道数
print(img.dtype)