import cv2
img = cv2.imread("alphabet.jpg", cv2.IMREAD_UNCHANGED)

start_x = 41
start_y = 14
width_of_pic = 99
height_of_pic = 121
width_of_blank = 3
height_of_blank = 28
for i in range(6):
    for j in range(4):
        x = start_x + j * width_of_pic + j * width_of_blank
        y = start_y + i * height_of_pic + i * height_of_blank
        print(x, y, end="|")
        region = img[y: y + height_of_pic, x: x + width_of_pic]
        region[-26: , 0:34] = [255, 255, 255]
        cv2.imshow(str(i)+"-"+str(j), region)
        # 保存图像
        # 三个参数分别对应保存的路径及文件名、图像矩阵、指定格式（对于JPEG，其表示的是图像的质量）
        # 用0-100的整数表示，默认为95。 注意，cv2.IMWRITE_JPEG_QUALITY类型为Long，必须转换成int；对于PNG，第三个参数表示的是压缩级别。cv2.IMWRITE_PNG_COMPRESSION，
        # 从0到9,数字越小,压缩级别越高,图像尺寸越小 这个是可选参数
        cv2.imwrite("images/alphabet/"+str(i)+"-"+str(j)+'.jpg', region, [int(cv2.IMWRITE_JPEG_QUALITY), 9])
    print()
cv2.waitKey(0)
