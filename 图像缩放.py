import cv2

img = cv2.imread("test.jpg", cv2.IMREAD_UNCHANGED)
#                         (多少列   行)    一定要是整数
dst_img = cv2.resize(img, (200, 150))
cv2.imshow("dst_img", dst_img)
dst_img = cv2.resize(img, None, fx=0.5, fy=0.7)    # 宽设置成原图像的0.5倍 高设置成原图像的0.7倍    None处填写希望缩放到的图像大小元组
cv2.imshow("dst_img_", dst_img)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

