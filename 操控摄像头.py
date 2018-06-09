import cv2
import numpy as np

cap = cv2.VideoCapture(0)    # 读取摄像头,0为摄像头索引.当有多个摄像头时从0开始编号
fourcc = cv2.VideoWriter_fourcc()



while True:
    ret, frame = cap.read()    # 从视频或摄像头中读取一帧（即一张图像),返回是否成功标识ret(True代表成功，False代表失败)
                               # frame为读取的视频帧
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("frame", frame)    # 显示视频帧
    cv2.imshow("gray", gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):    # 等候1ms,播放下一帧,或者按q键退出
        break

cap.release()    # 释放视频流
cv2.destroyAllWindows()