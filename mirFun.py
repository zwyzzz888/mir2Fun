import os
import sys

from datetime import datetime
import random
import win32api
import win32gui
import win32ui
import win32con
import aircv as ac
from ctypes import windll
import time

flag_random = True

def clickLeftCur():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def leftDown(pos, hd):  # 鼠标左键按下
    handle = hd
    client_pos = win32gui.ScreenToClient(handle, pos)
    tmp = win32api.MAKELONG(client_pos[0], client_pos[1])
    win32gui.SendMessage(handle, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
    win32gui.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp)


def leftUp(pos, hd):  # 鼠标左键抬起
    handle = hd
    client_pos = win32gui.ScreenToClient(handle, pos)
    tmp = win32api.MAKELONG(client_pos[0], client_pos[1])
    win32gui.SendMessage(handle, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
    win32gui.SendMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)


def rightDown(pos, hd):  # 鼠标右键按下
    handle = hd
    client_pos = win32gui.ScreenToClient(handle, pos)
    tmp = win32api.MAKELONG(client_pos[0], client_pos[1])
    win32gui.SendMessage(handle, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
    win32gui.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_RBUTTON, tmp)


def rightUp(pos, hd):  # 鼠标右键抬起
    handle = hd
    client_pos = win32gui.ScreenToClient(handle, pos)
    tmp = win32api.MAKELONG(client_pos[0], client_pos[1])
    win32gui.SendMessage(handle, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
    win32gui.SendMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_RBUTTON, tmp)


def click_it(pos, hd):
    handle = hd
    client_pos = win32gui.ScreenToClient(handle, pos)
    tmp = win32api.MAKELONG(client_pos[0], client_pos[1])
    win32gui.SendMessage(handle, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
    win32gui.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp)
    win32gui.SendMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)


def click_it_double(pos, hd):
    handle = hd
    client_pos = win32gui.ScreenToClient(handle, pos)
    tmp = win32api.MAKELONG(client_pos[0], client_pos[1])
    win32gui.PostMessage(handle, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
    win32gui.PostMessage(handle, win32con.WM_LBUTTONDBLCLK, win32con.MK_LBUTTON, tmp)
    # win32gui.PostMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)
    # time.sleep(0.1)
    # win32gui.PostMessage(handle, win32con.WM_LBUTTONDBLCLK, win32con.MK_LBUTTON, tmp)
    # win32gui.PostMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)
    # time.sleep(0.2)


def click_it_key(pos, hd, key):
    handle = hd
    # moveCurPos(pos[0], pos[1])

    client_pos = win32gui.ScreenToClient(handle, pos)
    tmp = win32api.MAKELONG(client_pos[0], client_pos[1])
    win32gui.SendMessage(handle, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
    # win32gui.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp)
    # win32gui.SendMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)
    win32gui.SendMessage(handle, win32con.WM_MOUSEMOVE, 0, tmp)
    # 116代表F5
    # win32api.keybd_event(key, 0, 0, 0)
    # win32api.keybd_event(key, 0, win32con.KEYEVENTF_KEYUP, 0) # 释放
    win32gui.SendMessage(handle, win32con.WM_KEYDOWN, key, 0)
    win32gui.SendMessage(handle, win32con.WM_KEYUP, key, 0)


def click_key(hd, key):
    handle = hd
    win32gui.PostMessage(handle, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
    win32gui.PostMessage(handle, win32con.WM_KEYDOWN, key, 0)
    win32gui.PostMessage(handle, win32con.WM_KEYUP, key, 0)


def click_key_esc(hd):
    handle = hd
    win32gui.PostMessage(handle, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
    win32gui.PostMessage(handle, win32con.WM_KEYDOWN, win32con.VK_ESCAPE, 0)
    win32gui.PostMessage(handle, win32con.WM_KEYUP, win32con.VK_ESCAPE, 0)


def click_key_prtsc(hd):
    handle = hd
    win32gui.PostMessage(handle, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
    win32gui.PostMessage(handle, win32con.WM_KEYDOWN, win32con.VK_PAUSE, 0)
    win32gui.PostMessage(handle, win32con.WM_KEYUP, win32con.VK_PAUSE, 0)


def click_it_a(pos, hd):
    handle = hd
    client_pos = win32gui.ScreenToClient(handle, pos)
    tmp = win32api.MAKELONG(client_pos[0], client_pos[1])
    win32gui.PostMessage(handle, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
    win32gui.PostMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp)
    win32gui.PostMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)


def moveCurPos(x, y):  # 移动鼠标
    windll.user32.SetCursorPos(x, y)


def getCurPos():  # 获得鼠标位置信息，这个再实际代码没用上，调试用得上
    return win32gui.GetCursorPos()


def dragCur(param, hd):  # 鼠标右键点击
    leftDown((param[0], param[1]), hd)
    leftUp((param[0], param[1]), hd)


def dragCurRight(param, hd):  # 鼠标右键点击
    rightDown((param[0], param[1]), hd)
    rightUp((param[0], param[1]), hd)


def match_img(imgsrc, imgobj, confidence):  # imgsrc=原始图像，imgobj=待查找的图片
    """
    :rtype: object
    """
    imsrc = ac.imread(imgsrc)
    imobj = ac.imread(imgobj)
    match_result = ac.find_template(imsrc, imobj, confidence)
    if match_result is not None:
        match_result['shape'] = (imsrc.shape[1], imsrc.shape[0])  # 0为高，1为宽
    return match_result


def window_capture(filename, hd):
    hwnd = hd  # 窗口的编号，0号表示当前活跃窗口
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 获取监控器信息
    MoniterDev = win32api.EnumDisplayMonitors(None, None)
    w = MoniterDev[0][2][2]
    h = MoniterDev[0][2][3]
    #print(w, h)#图片大小
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 截取从左上角（0，0）长宽为（w，h）的图片
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()


def window_capture_small(filename, hd):
    hwnd = hd  # 窗口的编号，0号表示当前活跃窗口
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # # 获取监控器信息
    # MoniterDev = win32api.EnumDisplayMonitors(None, None)
    # w = MoniterDev[0][2][2]
    # h = MoniterDev[0][2][3]

    x, y, w, h = win32gui.GetWindowRect(hwnd)


    #print(w, h)#图片大小
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 截取从左上角（0，0）长宽为（w，h）的图片
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()


hwnd_title = dict()


def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


def get():
    list = []
    win32gui.EnumWindows(get_all_hwnd, 0)
    for h, t in hwnd_title.items():
        if t != "":
            # if t == '夜神模拟器':
            if t == 'www.15 0o .com' and h == get_foreground_windows():
                rect = win32gui.GetWindowRect(h)
                x = rect[0]
                w = rect[2] - x
                if w > 0:   # 有两个窗口 获取窗口高度大于0的,这样不影响打字
                    list.append(h)
                    print(h)
                    return list
    return list


def getXYinWin(hwnd):  # GetCursorPos 获取鼠标指针的当前位置
        p = win32api.GetCursorPos()
        print(p[0], p[1])
        #  GetWindowRect 获得整个窗口的范围矩形，窗口的边框、标题栏、滚动条及菜单等都在这个矩形内 
        x, y, w, h = win32gui.GetWindowRect(hwnd)
        print("x, y, w, h")
        print(x, y, w, h)
        # 鼠标坐标减去指定窗口坐标为鼠标在窗口中的坐标值
        pos_x = p[0] - x
        pos_y = p[1] - y
        print("pos_x,pos_y")
        print(pos_x, pos_y)
        return pos_x, pos_y


def get_foreground_windows():
    return win32gui.GetForegroundWindow()


def temp_size(hd):
    win32gui.GetForegroundWindow()
    # win32gui.MoveWindow(hd, 0, 0, 1024, 780, True)
    pri = win32gui.GetWindowLong(hd,win32con.GWL_EXSTYLE)

    win32gui.SetWindowLong(hd, win32con.GWL_EXSTYLE, win32con.WS_CAPTION)
    win32gui.SetWindowPos(hd, None, 0,0,0,0, 127)


def mouse_move_and_click(pos):  # 前台移动鼠标
    win32api.SetCursorPos(pos)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, pos[0], pos[1], 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, pos[0], pos[1], 0, 0)


def mouse_move_to_sell(hd):   # 移动鼠标卖东西操作无法后台,使用前台命令
    if hd == win32gui.GetForegroundWindow():
        x, y, w, h = win32gui.GetWindowRect(hd)
        # 318,286  物品位置   359, 358 ok位置
        pos = win32api.GetCursorPos()
        print(pos)
        tmp = pos
        mouse_move_and_click(pos)
        time.sleep(0.1)
        pos = x + 316, y + 291
        mouse_move_and_click(pos)
        time.sleep(0.1)
        pos = x + 316 + 42, y + 291 + 65
        mouse_move_and_click(pos)
        time.sleep(0.1)
        mouse_move_and_click(tmp)  # 恢复鼠标位置
        print(tmp)


def train_skill_f7(hwnd, pos):
    # rect = win32gui.GetWindowRect(hwnd)
    # 鼠标坐标加去指定窗口坐标为鼠标在窗口中的坐标值
    # move_x = rect[0] + 645
    # move_y = rect[1] + 335
    # print(move_x, move_y)
    click_it_key(pos, hwnd, win32con.VK_F7)


def train_skill_f8(hwnd, pos):
    baseImg = "./pic/blackground.jpg"  # 储存的文件名  # 储存的文件名
    rect = win32gui.GetWindowRect(hwnd)
    # window_capture(baseImg, hwnd)  # 对整个屏幕截图，并保存截图为baseImg
    window_capture_small(baseImg, hwnd)  # 对整个屏幕截图，并保存截图为baseImg
    # 遍历所有图片
    for filename in os.listdir(r"./pic/images"):  # listdir的参数是文件夹的路径
        imagePath = "./pic/images/" + filename
        res = match_img(baseImg, imagePath, 0.7)
        if res is None:
            continue
        if filename == "reward.png":
            x = rect[0] + 20
            y = rect[1] + 560
        else:
            x = rect[0] + res["result"][0]
            y = rect[1] + res["result"][1]
        # move_x = random.randint(int(x) - 2, int(x) + 2)
        # move_y = random.randint(int(y) - 2, int(y) + 2)
        move_x = int(x)
        move_y = int(y)
        click_it((move_x, move_y), hwnd)          # 这里双击调试了半天 最后还是不知道怎么实现的 反正就是成功了,虽然不知道逻辑是什么但是功能实现了O.O
        click_it_double((move_x, move_y), hwnd)
        time.sleep(0.2)
        click_it_double((move_x, move_y), hwnd)
        click_it((move_x, move_y), hwnd)
    imagePath2 = "./pic/" + "kulou.png"
    res2 = match_img(baseImg, imagePath2, 0.8)
    if res2 is None:
        print("骷髅没找到")
        click_it_key(pos, hwnd, win32con.VK_F8)
    time.sleep(5)


def get_death_pic(hwnd):
    time.sleep(3)
    baseImg = "./pic/blackground.jpg"  # 储存的文件名  # 储存的文件名
    rect = win32gui.GetWindowRect(hwnd)
    window_capture_small(baseImg, hwnd)  # 对整个屏幕截图，并保存截图为baseImg
    # 遍历所有图片
    imagePath = "./pic/siwang2.png"
    res = match_img(baseImg, imagePath, 0.99)
    if res is None:
        print("没死亡")
        return
    else:
        # 按下截图，并退出本程序
        print("死亡了")
        window_capture_small("./pic/" + time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time())) + ".jpg", hwnd)  # 对整个屏幕截图，获取死亡时间
        click_key_prtsc(hwnd)
        os._exit(0)


pos_randomX = [504, 601, 622, 588, 501, 407, 391, 415]
pos_randomY = [233, 281, 358, 416, 432, 404, 350, 277]


def auto_run_random(hwnd, event):
   rect = win32gui.GetWindowRect(hwnd)
   #  选择一个随即方向
   random_number = random.randint(0, 7)
   #  TODO 优化随即方式 让移动范围更大
   x = rect[0] + pos_randomX[random_number]
   y = rect[1] + pos_randomY[random_number]
   if random_number == 7:
       random_number = 0
   else:
       random_number = random_number + 1
   x2 = rect[0] + pos_randomX[random_number]
   y2 = rect[1] + pos_randomY[random_number]
   #  随即走的步数
   step_num = random.randint(15, 40)
   for i in range(step_num):
    if event.is_set():  # 中断线程用
        return
    if check_odd_even(i):  # 走两步 一拐弯
        dragCurRight((x, y), hwnd)
    else:
        dragCurRight((x2, y2), hwnd)
    time.sleep(0.8)
    #  判断下是否要使用随即
    global flag_random
    if bool_run_random(get_current_min()) == 1 and flag_random:  # 当时间的分钟为5的倍数时候,并且标记为True 按6使用随即 同时将标记置为False
        click_key(hwnd, 54) # 6是54 搜索虚拟键码对照表
        flag_random = False
        print("test bool_run_random随即了" + str(get_current_min()) + str(flag_random))
    elif bool_run_random(get_current_min()) == 2 and not flag_random:  # 当时间的分钟为5的倍数+1的时候,并且标记为False,将标记置为True,以便下次继续随即
        flag_random = True
        print("test bool_run_random恢复了" + str(get_current_min()) + str(flag_random))


def check_odd_even(number):
    if number % 3 == 0:
        return True
    else:
        return False


def bool_run_random(number):
    if number % 15 == 0:
        return 1
    elif number % 15 == 1:
        return 2
    else:
        return 0

# 获取当前时间分钟数
def get_current_min():
    current_time = datetime.now()
    # 提取分钟数
    return current_time.minute


def loop(hwnd):
    rect = win32gui.GetWindowRect(hwnd)
    # 鼠标坐标加去指定窗口坐标为鼠标在窗口中的坐标值
    move_x = rect[0] + 840
    move_y = rect[1] + 335
    print("鼠标坐标加去指定窗口坐标为鼠标在窗口中的坐标值")
    print(move_x, move_y)
    click_it((move_x, move_y), hwnd)


def main2():
    print("欢迎来到阴阳师联盟！")
    arg = 0
    tt = 2
    # if sys.argv.__len__() > 1:  #多人组队
    #     arg = sys.argv[1]
    # else:
    #     tt = 1
    # 获取所有阴阳师句柄
    list = get()

    # list = [395746, 263310]
    while True:
        time.sleep(tt)  # 设置隔2秒运行一次
        # 循环所有句柄
        for hd in list:
            loop(hd)

# if __name__=="__main__":
#     main()





