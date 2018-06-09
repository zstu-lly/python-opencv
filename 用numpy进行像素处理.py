import cv2
img = cv2.imread("test.jpg", cv2.IMREAD_UNCHANGED)
cv2.imshow("original", img)
print(img.item(100, 100, 0))
img.itemset((100, 100, 0), 0)    # 更改像素值
print(img.item(100, 100, 0))
cv2.imshow("result", img)
cv2.waitKey(0)