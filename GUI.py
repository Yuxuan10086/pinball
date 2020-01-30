from tkinter import *
import tkinter.font as tkFont

root = Tk()
root.geometry('500x100')
root.title('很迷的一个窗口,不要犹豫,直接关了就行')
#虽然我也不知道这个窗口有什么卵用,但是删了之后就会报错

def about():   #"关于"窗口 介绍作者 出示版权声明
    about = Tk()
    about.geometry('500x300')
    about.title('About')
    about.resizable(False, False)
    '''
    未完成,仅空白窗口
    '''
    about.mainloop()

def wait_win(get_q): # 进度条窗体
    longth = 0
    wait = Tk()
    wait.title('Wait...')
    wait.geometry('560x150')

    Label(wait, text = '稍等,正在生成...', font = ft).place(x = 50, y = 35)
    canvas = Canvas(wait, width = 465, height = 22, bg = "white")
    canvas.place(x = 50, y = 60)

    while longth < 500:
        longth = get_q.get()
        canvas.coords(canvas, (0, 0, 600, 60))
        wait.update()

def wait(txt, r): # 真正的wait
    from queue import Queue
    from threading import Thread
    import encryption as en
    q = Queue()
    t1 = Thread(target = en.fast, args=(txt, r, ))
    t2 = Thread(target = wait_win, args=(q,))
    t2.start()
    t1.start()
    '''
    蛋疼的是仅仅fast函数正常运行
    wait窗口却无法弹出
    而且结果生成后程序仍无响应
    爷累了
    明天再解决
    '''

def main():  # 用户输入数据窗口
    def act():
        txt = inputt.get('0.0', 'end')
        r = len(txt) / 5
        wait(txt, r)
        main.quit()
        '''
        可优化之处:quit无法在wait打开的同时关闭
        '''

    main = Tk()
    main.geometry('500x300')
    main.title('弹球加密')
    main.resizable(False, False)

    inputt = Text(main, font = ft)
    inputt.place(width = 500, height = 50)
    start = Button(main, command = act, text = '开始', font = ft)
    start.pack(side = 'bottom')

    main.mainloop()


ft = tkFont.Font(family = 'Fixdsys', size = 20) # 设置字体

main()

