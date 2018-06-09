import cv2
import numpy as np

img = cv2.imread("test.jpg", cv2.IMREAD_UNCHANGED)

cv2.line(img, (0, 0), (150, 150), (255, 255, 255), 10)    # 图像 起点 终点 颜色 粗细
cv2.rectangle(img, (15, 15), (200, 300), (0, 255, 0), 5)
cv2.circle(img, (50, 50), 30, (0, 0, 255), -1)    # -1表示填充圆

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
cv2.polylines(img, [pts], True, (0, 255, 255), 5)    # 图像 点集 是否首尾相连 颜色 粗细

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCv Tuts!', (0, 130), font, 1, (200, 255, 255), 2, cv2.LINE_AA)    # 图像 内容 位置 字体 字体大小 颜色 字体粗细 字间距

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
