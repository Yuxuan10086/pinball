def find_center(x, y, v, size):
    #传入当前位置(imt),速度(int)与图像大小(数组),返回数组数组坐标
    import random as ra
    k = ra.uniform(-2, 2)
    b = y - k * x
    res = []
    while(x <= size[0] and y <= size[1]):
        y = int(k * x + b)
        res.append([x, y])
        x += v
    return res
# a = find_center(0, 0, 5, [30, 50])
# print(a)
def draw(txt):  #传入不分行的字符串,返回白底红字图片,以十个字符为一行分割
    import cv2 as cv
    import numpy as np
    from PIL import Image, ImageDraw, ImageFont
    y = len(txt) // 10 * 40 + 40
    for i in range(len(txt) // 10):
        txt = txt[0: i * 10 + 10 + i] + '\n' + txt[i * 10 + 10 + i:]
    img = np.zeros([y, 500, 3], np.uint8)
    for i in range(y - 1):
        for j in range(500):
            img[i][j] = [255, 255, 255]
    cv2img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    pilimg = Image.fromarray(cv2img)
    draw = ImageDraw.Draw(pilimg)
    font = ImageFont.truetype("simhei.ttf", 40, encoding="utf-8")
    draw.text((0, 0), txt, (255, 0, 0), font=font)
    res = cv.cvtColor(np.array(pilimg), cv.COLOR_RGB2BGR)
    return res
# draw('你你你你你你男男女女你你你你你你男男女女')
def black(cen_x, cen_y, r, img):  #传入圆心(int),半径(int)与图像,返回涂黑后的图片
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if (j - cen_x) ^ 2 + (i - cen_y) ^ 2 > r ^ 2:
                img[i][j] = [0, 0, 0]
    return img
a = black(0, 0, 50, draw('你你你你你你男男女女你你你你你你男男女女'))
import cv2
import numpy as np
cv2.imshow('hh', a)
cv2.waitKey(0)
