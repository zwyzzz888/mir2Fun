
import threading

from pynput import keyboard
import time
import mirFun


# Key.alt_l    m    Key.f8
flag_case_train_skill_normal = False  # 练习普通技能状态标识
flag_case_train_skill_taoist = False  # 练习道士技能状态标识 需要换符
flag_case_auto_run_romdon = False  # 随便跑步开关
global flag_train_skill_taoist_windows
global flag_run_windows
flag_case_case_auto_pick = False  # 自动拾取状态标识
flag_case_death_pic = False  # 自动死亡截图
flag_case_run = False  # 练习普通技能状态标识
pos_case_train_skill_normal = []
pos_case_run = []
record_key = []  # 临时记录按键,用于检测当前按键组合键
hd_list = []  # 记录窗口句柄
event = threading.Event()


def case_sell_or_save():                            # 自动卖东西
    print('sell_or_save')
    for hd in hd_list:
        mirFun.mouse_move_to_sell(hd)


def auto_pick(hd):    # 自动拾取
    global flag_case_case_auto_pick
    if flag_case_case_auto_pick:
        time.sleep(0.8)
        mirFun.click_key_esc(hd)


def case_auto_pick():                            # 自动拾取
    print('case_auto_pick')
    global flag_case_case_auto_pick
    if flag_case_case_auto_pick:
        flag_case_case_auto_pick = False
        print('case_auto_pick关闭')
    else:
        flag_case_case_auto_pick = True
        print('case_auto_pick开启')


def case_off():                            # 小退关闭标识
    print('小退')
    global flag_case_case_auto_pick
    flag_case_case_auto_pick = False
    global flag_case_auto_run_romdon
    flag_case_auto_run_romdon = False

def case_auto_death_pic():                            # 自动死亡截图
    print('死亡截图')
    global flag_case_death_pic
    if flag_case_death_pic:
        flag_case_death_pic = False
        print('死亡截图关闭')
    else:
        flag_case_death_pic = True
        auto_death_pic(hd_list[0])
        print('死亡截图开启')


def auto_pick_nomarl(hd):   # 自动练习技能 诱惑bb之类的
    global flag_case_train_skill_normal
    if flag_case_train_skill_normal:
        time.sleep(0.3)
        mirFun.train_skill_f7(hd, pos_case_train_skill_normal)


def run_train_skill_f8(hd):   # 线程要执行的方法 自动道士会换符
    while flag_case_train_skill_taoist:
        mirFun.train_skill_f8(hd, pos_case_train_skill_normal)


def run_auto_run_random(hd, event):   # 线程要执行的方法 自动跑路
    while flag_case_auto_run_romdon:
        mirFun.auto_run_random(hd, event)


def auto_pick_shidao(hd):   # 自动练习技能 道士会换符
    global flag_case_train_skill_taoist
    global flag_train_skill_taoist_windows
    if flag_case_train_skill_taoist and (hd == flag_train_skill_taoist_windows):
        t = threading.Thread(target=run_train_skill_f8, args=(hd,))
        t.start()


def auto_run_random(hd, event):   # 自动跑路
    global flag_case_auto_run_romdon
    if flag_case_auto_run_romdon:
        event.clear()
        t = threading.Thread(target=run_auto_run_random, args=(hd, event,))
        t.start()
    else:
        print("停止自动跑路")
        event.set()


def run_get_death_pic(hd):   # 线程要执行的方法 自动死亡截图
    while flag_case_death_pic:
        mirFun.get_death_pic(hd)


def auto_death_pic(hd):   # 自动死亡截图
    global flag_case_death_pic
    if flag_case_death_pic:
        t = threading.Thread(target=run_get_death_pic, args=(hd,))
        t.start()


def case_train_skill_nomorl():                            # 自动练习技能 诱惑bb之类的
    print('train_skill')
    global flag_case_train_skill_normal
    global pos_case_train_skill_normal
    if flag_case_train_skill_normal:
        flag_case_train_skill_normal = False
        print('train_skill关闭')
    else:
        flag_case_train_skill_normal = True
        pos_case_train_skill_normal = mirFun.getCurPos()
        print('train_skill开启')


def case_train_skill_taoist():                            # 可以自动换符的道士练技能
    print('train_skill_taoist')
    global flag_case_train_skill_taoist
    global pos_case_train_skill_normal
    global flag_train_skill_taoist_windows
    if flag_case_train_skill_taoist:
        flag_case_train_skill_taoist = False
        print('train_skill_f8关闭')
    else:
        flag_case_train_skill_taoist = True
        pos_case_train_skill_normal = mirFun.getCurPos()
        flag_train_skill_taoist_windows = mirFun.get_foreground_windows()
        # mirFun.temp_size(flag_train_skill_taoist_windows)
        auto_pick_shidao(hd_list[0])
        print('train_skill_f8开启')


def case_auto_run_random():                            # 自动跑路
    print('auto_run_random')
    global flag_case_auto_run_romdon
    global pos_case_train_skill_normal
    global event
    if flag_case_auto_run_romdon:
        flag_case_auto_run_romdon = False
        auto_run_random(hd_list[0], event)
        print('auto_run_random关闭')
    else:
        flag_case_auto_run_romdon = True
        pos_case_train_skill_normal = mirFun.getCurPos()
        # mirFun.temp_size(flag_train_skill_taoist_windows)
        auto_run_random(hd_list[0], event)
        print('auto_run_random开启')


def auto_run(hd):   # 自动选择方向奔跑
    global flag_case_run
    if flag_case_run:
        time.sleep(0.3)


def case_default():                          # 默认情况下执行的函数
    print('No such case')


switch = {"'m'": case_sell_or_save,                # 注意此处不要加括号
          "'Key.f7'": case_train_skill_nomorl,
          "'Key.f8'": case_train_skill_taoist,
          "'Key.esc'": case_train_skill_taoist,
          "'Key.f10'": case_auto_run_random,
          }


def run_someting(key_str):     # 执行方法
    # 如果激活的是当前的窗口再执行方法  可以多开
    if len(hd_list) > 0 and hd_list[0] == mirFun.get_foreground_windows():
        # print("key_str=" + key_str)
        if "'m'" == key_str:
            case_sell_or_save()
        elif "Key.f7" == key_str:
            case_train_skill_nomorl()
        elif "Key.f8" == key_str:
            case_train_skill_taoist()
        elif "Key.esc" == key_str:
            case_auto_pick()
        elif "Key.f11" == key_str:
            case_auto_death_pic()
        elif "Key.f10" == key_str:
            case_auto_run_random()
        elif "'x'" == key_str:
            case_off()
    elif "Key.f12" == key_str:
        init_hd()


def on_press(key):
    """定义按下时候的响应，参数传入key"""
    try:
        # print(f'{key.char} down')
        pass
    except AttributeError:
        print(f'{key} down')
    if(str(key) not in record_key):
        record_key.append(str(key))
    if ('Key.alt_l' in record_key):
        run_someting(str(key))


def on_release(key):
    """定义释放时候的响应"""
    # print(f'{key} up')
    # print(record_key)
    if str(key) in record_key:
        record_key.remove(str(key))


def on_move(x, y):
    print('move to', x, y)


# 鼠标监听 暂时不需要
# def on_click(x, y, button, pressed):
#     print('click at', x, y, button, pressed)
#
#
# def on_scroll(x, y, dx, dy):
#     print('scroll at', x, y, 'by', dx, dy)


# 监听写法1
def listen_key_block():
    with keyboard.Listener(
            on_press=on_press, on_release=on_release) as listener:
        listener.join()  # 加入线程池，阻塞写法


# 监听写法2
def listen_key_nblock():
    listener = keyboard.Listener(
        on_press=on_press, on_release=on_release
    )
    listener.start()  # 启动线程


# def listen_mouse_nblock():
#     listener = mouse.Listener(
#         on_move=None,  # 因为on_move太多输出了，就不放进来了，有兴趣可以加入
#         on_click=on_click,
#         on_scroll=on_scroll
#     )
#     listener.start()


def init_hd():
    print("窗口初始化")
    global hd_list
    if len(hd_list) > 0:
        print("窗口已经初始化，要重置窗口请重启程序")
        return
    hd_list = mirFun.get()
    print("窗口初始化获取窗口数量:" + str(len(hd_list)))
    # if not windll.shell32.IsUserAnAdmin():
        # 不是管理员就提权
        # windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)



if __name__ == '__main__':
    # listen_mouse_nblock()
    listen_key_nblock()
    print("以下功能都是模拟键鼠操作，不影响游戏平衡性")
    print("以下功能都是模拟键鼠操作，不影响游戏平衡性")
    print("以下功能都是模拟键鼠操作，不影响游戏平衡性")
    print("以下功能都是模拟键鼠操作，不影响游戏平衡性")
    print("使用方法介绍：")
    print("先启动游戏，在窗口激活的状态下，alt + f12 初始化窗口，只适合1024 分辨率 未适配 800分辨率")
    print("如果多开，就依次开游戏再依次启动多个本程序，使用快捷键时候，保证游戏窗口激活再按功能快捷键")
    print("alt + esc 自动显示物品，拾取物品，其实就是不停的按esc，如果组队的时候需要临时关闭，再按次就关闭，以下同理")
    print("alt + f7  自动训练技能，把技能设置为f7键释放，鼠标指向需要释放的地方，按下即可，再按停止，只能适合诱惑等技能，不适合道士需要换符的技能")
    print("alt + f8  5s换一次符，设置为f8，打开包裹，包裹里面装好符，物品窗口拖动到右边，点开人物窗口再关闭，配合f7使用")
    print("alt + m  (启动时窗口需要在前台)自动卖、存、修 物品， 点开卖、修、仓库保管窗口后，鼠标指向物品 按快捷键即可")
    print("alt + f10 随机行走(可以后台)")
    while True:  # 这里应该用一个循环维持主线程，否则主线程结束了子线程就自动结束了，只是为了
        # 注意电脑也是需要缓冲的，不可一下子同时点击又打字又松开，中间可适当用time.sleep()函数来进行缓冲。
        time.sleep(0.02)  # 缓冲0.01s
        # 循环所有句柄
        for hd in hd_list:
            auto_pick(hd)
            auto_pick_nomarl(hd)
            # auto_pick_shidao(hd)
        pass
