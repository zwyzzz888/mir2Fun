import ctypes
from ctypes.wintypes import POINT  # 导入 POINT 类型
import os
# from ctypes import Structure, c_long, c_char, c_uint, c_short, c_ushort, c_ulong
from datetime import datetime
import random

import aircv as ac
import win32api
import win32gui
import win32ui
import win32con
import time

# 初始化 DPI 感知
try:
    ctypes.windll.user32.SetProcessDPIAware()
except AttributeError:
    # 对于不支持 SetProcessDPIAware 的系统（如 Windows XP），忽略该错误
    pass

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
    # win32gui.PostMessage(handle, win32con.WM_KEYDOWN, win32con.VK_ESCAPE, 0)
    win32gui.PostMessage(handle, win32con.WM_KEYDOWN, 0xC0, 0)
    win32gui.PostMessage(handle, win32con.WM_KEYUP, 0xC0, 0)
    # win32gui.PostMessage(handle, win32con.WM_KEYUP, win32con.VK_ESCAPE, 0)


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
    ctypes.windll.user32.SetCursorPos(x, y)


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
    # TODO 注释掉了打包让体积更小
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


def get_window_monitor_scaling(hwnd):
    """获取指定窗口所在显示器的缩放比例（DPI）"""
    # 获取窗口位置和大小
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    center_x = (left + right) // 2
    center_y = (top + bottom) // 2

    # 创建 POINT 结构体并填充数据
    point = POINT(center_x, center_y)

    # 获取窗口所在的显示器
    monitor = ctypes.windll.user32.MonitorFromPoint(
        point,  # 使用 POINT 结构体
        2  # MONITOR_DEFAULTTONEAREST
    )
    if not monitor:
        raise RuntimeError('无法获取显示器信息')

    # 获取显示器的 DPI
    dpi_x = ctypes.c_uint()
    dpi_y = ctypes.c_uint()
    ctypes.windll.shcore.GetDpiForMonitor(monitor, 0, ctypes.byref(dpi_x), ctypes.byref(dpi_y))

    # 计算缩放比例
    scaling_x = dpi_x.value / 96.0
    scaling_y = dpi_y.value / 96.0

    return (scaling_x + scaling_y) / 2


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
            # if t == 'www.15 0o .com' and h == get_foreground_windows():
            if h == get_foreground_windows():
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
    pos_sell = [316, 291] # 物品位置
    pos_ok = [316 + 42, 291 + 65] # ok位置
    scaling = get_window_monitor_scaling(hd)
    if hd == win32gui.GetForegroundWindow():
        x, y, w, h = win32gui.GetWindowRect(hd)
        # 测试坐标用
        # getXYinWin(hd)
        pos = win32api.GetCursorPos()
        # print(pos)
        tmp = pos
        mouse_move_and_click(pos)
        time.sleep(0.1)
        pos = x + round(pos_sell[0]*scaling), y + round(pos_sell[1]*scaling)
        mouse_move_and_click(pos)
        time.sleep(0.1)
        pos = x + round(pos_ok[0]*scaling), y + round(pos_ok[1]*scaling)
        mouse_move_and_click(pos)
        time.sleep(0.1)
        mouse_move_and_click(tmp)  # 恢复鼠标位置
        # print(tmp)


def mouse_move_to_trade(hd):   # 移动鼠标交易操作无法后台,使用前台命令
    pos_sell = [716, 262] # 交易框位置
    scaling = get_window_monitor_scaling(hd)
    if hd == win32gui.GetForegroundWindow():
        x, y, w, h = win32gui.GetWindowRect(hd)
        # #测试坐标用
        # getXYinWin(hd)
        pos = win32api.GetCursorPos()
        # print(pos)
        tmp = pos
        mouse_move_and_click(pos)
        time.sleep(0.1)
        pos = x + round(pos_sell[0]*scaling), y + round(pos_sell[1]*scaling)
        mouse_move_and_click(pos)
        time.sleep(0.1)
        mouse_move_and_click(tmp)  # 恢复鼠标位置
        # print(tmp)


def train_skill_f7(hwnd, pos, key_value):
    click_it_key(pos, hwnd, key_value)


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
    try:
        res2 = match_img(baseImg, imagePath2, 0.8)
        if res2 is None:
            print("骷髅没找到")
            click_it_key(pos, hwnd, win32con.VK_F8)
        time.sleep(5)
    except:
        print("/pic/kulou.png 不存在")
        pass

# def get_current_gamma_ramp():
#     """
#     获取当前屏幕的伽马值
#     返回: (red_gamma, green_gamma, blue_gamma) 的元组
#     """
#     # 创建空数组用于存储当前伽马值
#     gamma_array = (ctypes.c_ushort * 768)()
#
#     # 获取当前伽马值
#     ctypes.windll.gdi32.GetDeviceGammaRamp(ctypes.windll.user32.GetDC(0), gamma_array)
#
#     # 将伽马值转换为numpy数组便于处理
#     gamma = numpy.array(gamma_array)
#
#     # 分离RGB通道
#     r = gamma[0:256]
#     g = gamma[256:512]
#     b = gamma[512:768]
#
#     # 计算每个通道的伽马值(近似)
#     def calculate_gamma(channel):
#         # 找到中间值(避免极端值影响)
#         mid = channel[128]
#         if mid == 0:
#             return 1.0
#         return (mid / (128 * 256)) ** (-1)
#
#     return (calculate_gamma(r), calculate_gamma(g), calculate_gamma(b))


def set_current_gamma_ramp(red=1.0, green=1.0, blue=1.0, brightness=1.0):
    """
    设置屏幕伽马值和亮度
    :param red: 红色通道伽马值 (建议0.1-3.0)
    :param green: 绿色通道伽马值 (建议0.1-3.0)
    :param blue: 蓝色通道伽马值 (建议0.1-3.0)
    :param brightness: 整体亮度系数 (0.0-1.0)
    """
    # 创建伽马数组
    gamma_array = (ctypes.c_ushort * 768)()
    # 获取屏幕设备上下文
    # hdc = ctypes.windll.gdi32.CreateDCW(ctypes.c_wchar_p("DISPLAY"), None, None, None)
    hdc = ctypes.windll.user32.GetDC(None)
    if hdc == 0:
        raise RuntimeError("无法获取设备上下文")

    print(hdc)
    # 填充伽马数组
    for i in range(256):
        # 应用伽马校正和亮度调整
        gamma_array[i] = min(65535, max(0, int((i / 255.0) ** (1.0 / red) * 65535 * brightness)))
        gamma_array[i + 256] = min(65535, max(0, int((i / 255.0) ** (1.0 / green) * 65535 * brightness)))
        gamma_array[i + 512] = min(65535, max(0, int((i / 255.0) ** (1.0 / blue) * 65535 * brightness)))

    # 调用Windows API设置伽马值
    # result = ctypes.windll.gdi32.SetDeviceGammaRamp(hdc, ctypes.byref(gamma_array))
    # 尝试设置主显示器的伽马值
    success = ctypes.windll.gdi32.SetDeviceGammaRamp(hdc, ctypes.byref(gamma_array))

    # 清理设备上下文
    ctypes.windll.user32.ReleaseDC(None, hdc)

    if not success:
        raise RuntimeError("无法设置伽马值，可能不支持多显示器配置")

    # # 清理设备上下文
    # ctypes.windll.gdi32.DeleteDC(hdc)


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


# 左边从0点开始转
# 实在
# pos_randomX = [504, 621, 642, 608, 501, 387, 371, 415]
# pos_randomY = [203, 261, 358, 436, 452, 424, 350, 277]


# 火炬
pos_randomX = [515, 562, 564, 565, 515, 465, 466, 468]
pos_randomY = [256, 276, 318, 353, 357, 365, 319, 285]


def auto_run_random(hwnd, event):
   rect = win32gui.GetWindowRect(hwnd)
   #  选择一个随即方向
   random_number = random.randint(0, 7)
   # print("random_number=" + str(random_number))
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
   # step_num = random.randint(5, 6)
   step_num = random.randint(15, 40)
   for i in range(step_num):
    if event.is_set():  # 中断线程用
        print("中断线程用")
        return
    if check_odd_even(i):  # 走两步 一拐弯
        dragCurRight((x, y), hwnd)
    else:
        dragCurRight((x2, y2), hwnd)
    time.sleep(0.8)
    time.sleep(1.2)
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


def set_light(hd):
    win32api.SetDllDirectory()


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





