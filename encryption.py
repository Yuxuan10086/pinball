from queue import Queue
out = 0  # 此变量旨在给进度条程序传输程序完成度数据,num变量辅助其运行

def find_center(x, y, v, size, num, out_q):
    # 传入当前位置(int),速度(int)与图像大小(数组),返回数组数组坐标
    global out # 令out为全局变量
    import random as ra
    k = ra.uniform(-10, 10)
    # print(k)
    b = y - k * x
    res = []
    flag = []
    while(1):
        if x + v <= size[0]:
            flag.append(1)
        else:
            flag.append(0)
        if flag[0]:
            x += v
        else:
            x -= v
        y = int(k * x + b)
        if not (x <= size[0] and y <= size[1] and x >= 0 and y >= 0):
            break
        res.append([x, y])
    out += 500 / num
    out_q.put(out)
    return res

def draw(txt):  # 传入不分行的字符串,返回白底红字图片,以十个字符为一行分割
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

def black(cen_x, cen_y, r, img):  # 传入圆心(int),半径(int)与图像,返回涂黑后的图片
    # print(img.shape[0], img.shape[1])
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if (j - cen_x) ** 2 + (i - cen_y) ** 2 > r ** 2:
                img[i][j] = [0, 0, 0]
    return img




def save(txt, r, q, num = 100):
    import copy
    import cv2 as cv
    import imageio
    import os
    import shutil
    try:
        os.makedirs('img')
    except FileExistsError:
        pass
    pho = draw(txt)
    pho_0 = copy.deepcopy(pho)  # black函数的参数为数组,是可变类型,在函数中修改值会影响变量本身
    x = 0
    y = 0
    j = 0
    image_list = []
    while 1:
        cen = find_center(x, y, 10, [pho.shape[1], pho.shape[0]], num, q) # 调整刷新速度
        for i in range(len(cen)):
            cv.imwrite('img\\' + str(j)+ '_' + str(i) + '.jpg', black(cen[i][0], cen[i][1], r, pho_0))
            # 调整圆圈大小, 字数/5 此数值较佳
            pho_0 = copy.deepcopy(pho)
            image_list.append('img\\' + str(j)+ '_' + str(i) + '.jpg')
        print(cen)
        try:
            x = cen[-1][0]
            y = cen[-1][1]
        except IndexError:
            x = 0
            y = 0
        j += 1
        if j == num: # 调整生成图像数量
            break
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    imageio.mimsave('gif//res.gif', frames, 'GIF', duration = 0.1)  # 此处调整GIF播放速度
    # 务必提醒用户及时取出结果gif\res.gif,否则下一次使用将会覆盖原先结果
    shutil.rmtree('img')
    return 0


def fast(txt, r): # 使用多线程
    from threading import Thread
    q = Queue()
    t = Thread(target = save, args=(txt, r, q, ))
    t.start()

# save('你你你你你你男男女女你你你你你你男男女女你你你你你你男男女女你你你你你你男男女女你你你你你你男男女女你你你你你你男男女女你你你你你你男男女女你你你你你你男男女女你你你你你你男男女女你你你你你你男男女女你你你你你你男男女女你你你你你你男男女女')

# fast('你你你你你你男男女女你你你你你你男男女女你你你你你你男男女女你你你你你你男男女女你你你你你你男男女女你你你你你你'
#      '男男女女你你你你你你男男女女你你你你你你男男女女你你你你你你男男女女你你你你你你男男女女你你你你你你男男女女'
#      '你你你你你你男男女女', 25)