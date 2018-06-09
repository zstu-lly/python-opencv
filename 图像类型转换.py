import cv2

original_img = cv2.imread("test.jpg", cv2.IMREAD_UNCHANGED)
# 将BGR转换成RGB
result_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)    # (原图像, 要转换的类型)
cv2.imshow("original_img", original_img)
result_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)    # 灰度图像转BGR图像
cv2.imshow("result_img", result_img)
cv2.imwrite("test_gray.jpg", result_img)
print(result_img.shape)
print(original_img.shape)
cv2.waitKey(10000)