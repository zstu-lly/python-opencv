import cv2

img = cv2.imread("xiebiao.png", cv2.IMREAD_UNCHANGED)

grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, threshold = cv2.threshold(grayscaled, 220, 255, cv2.THRESH_BINARY)

gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)    # 自适应阈值二值化




cv2.imshow("gaus", gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()