import cv2

img = cv2.imread("test_gray.jpg", cv2.IMREAD_UNCHANGED)
return_val_, binary_img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)    # 二值化 将灰度值低于128的变为0 高于128的变为255
return_val_inv, binary_img_inv = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)    # 反二值化
return_val_trunc, trunc_img = cv2.threshold(img, 128, 255, cv2.THRESH_TRUNC)    # 截断亮度过大的 将灰度值高于128的变为128
return_val_to_zero, to_zero_img = cv2.threshold(img, 128, 255, cv2.THRESH_TOZERO)    # 将灰度值低于128的像素点变为0
return_val_to_zero_inv, to_zero_inv_img = cv2.threshold(img, 128, 255, cv2.THRESH_TOZERO_INV)    # 将灰度值高于128的像素点变为0
cv2.imshow("img", img)
cv2.imshow("binary_img", binary_img)
cv2.imshow("binary_img_inv", binary_img_inv)
cv2.imshow("trunc_img", trunc_img)
cv2.imshow("to_zero_img", to_zero_img)
cv2.waitKey()