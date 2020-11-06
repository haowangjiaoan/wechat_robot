# Author：Winter Liu is coming!
import cv2 as cv
import numpy as np
import pytesseract


# 预处理，高斯滤波（用处不大），4次开操作
# 过滤轮廓唯一
def contour_demo(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.GaussianBlur(gray, (5, 5), 1)
    ref, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
    kernel = np.ones((9, 9), np.uint8)
    thresh = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=4)
    contours, hierachy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    print(len(contours))
    return contours


def capture(img):
    contours = contour_demo(img)
    # 轮廓唯一，以后可以扩展
    contour = contours[0]
    # 求周长，可在后面的转换中使用周长和比例
    print(cv.arcLength(contour,True))
    img_copy = img.copy()
    # 使用approxPolyDP，将轮廓转换为直线，22为精度（越高越低），TRUE为闭合
    approx = cv.approxPolyDP(contour, 22, True)
    # print(approx.shape)
    # print(approx)
    # cv.drawContours(img_copy, [approx], -1, (255, 0, 0), 15)
    n = []
    # 生产四个角的坐标点
    for x, y in zip(approx[:, 0, 0], approx[:, 0, 1]):
        n.append((x, y))
    p1 = np.array(n, dtype=np.float32)
    # 对应点
    p2 = np.array([(0, 0), (0, 1500), (1000, 1500), (1000, 0)], dtype=np.float32)
    M = cv.getPerspectiveTransform(p1, p2) # 变换矩阵
    # 使用透视变换
    result = cv.warpPerspective(img_copy, M, (0, 0))
    # 重新截取
    result = result[:1501, :1001]
    cv.imwrite(r"D:\ocr.png", result)
    return result


# 图像识别代码，需要预先下载安装开源工具包 pytesseract，配置环境变量
# pip install pytesseract
# 修改“C:\Python\Python37\Lib\site-packages\pytesseract\pytesseract.py”中“cmd”为绝对路径
def ocr_img(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 图像清晰度越高结果越精确，时间更长
    text = pytesseract.image_to_string(gray)
    print(text)


src = cv.imread(r"D:\page.jpg")
#res = capture(src)
ocr_img(src)
cv.waitKey(0)
cv.destroyAllWindows()
