import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 查表
    lower_color = np.array([0, 0, 0])
    upper_color = np.array([180, 255, 46])

    # 让lower_red和upper_red范围之间的变为白色 别的范围的变为黑色
    mask = cv2.inRange(hsv, lower_color, upper_color)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((5, 5), np.uint8)

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)    # 开操作背景无噪点
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)    # 闭操作识别到的区域无噪点

    cv2.imshow('frame', frame)
    cv2.imshow('res', res)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:  # Esc:27
        break

cv2.destroyAllWindows()
cap.release()
