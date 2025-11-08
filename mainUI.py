# -*- coding: utf-8 -*-
import os
import sys
import webbrowser

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtNetwork import QNetworkRequest, QNetworkAccessManager
from PyQt5.QtWidgets import QButtonGroup, QCheckBox

import mirFun
from soundFun import checkshutup, shutup_recover, shutup, checkprompt, start_prompt, prompt_recover
from uioutput import Ui_MainWindow
from PyQt5.QtCore import QTimer, QDateTime, QUrl

# 导入时间模块
from mir2_timer import calculate_refresh_time, update_refresh_time, copy_to_clipboard

gama_off = 1.0, 1.0, 1.0
gama_on = 2.0, 2.0, 2.0

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        global main_window_instance
        main_window_instance = self
        super(MainWindow, self).__init__(parent)

        # 设置icon
        bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        self.setWindowIcon(QtGui.QIcon(os.path.join(bundle_dir, "favicon.ico")))
        self.setupUi(self)  # 加载 UI 文件

        # 创建按钮组
        self.radio_group = QButtonGroup(self)
        self.radio_group.setExclusive(True)  # 设置为排他性按钮组
        # 将所有 QRadioButton 添加进同一个组
        self.radio_group.addButton(self.radioButton505)
        self.radio_group.addButton(self.radioButton1505)
        self.radio_group.addButton(self.radioButton1005)
        self.radio_group.addButton(self.radioButtonCustom)

        # 初始化变量
        self.re_time = None  # 记录刷新时间
        self.isRed = False   # 背景闪烁标志

        # 连接按钮信号
        self.id_result_button.clicked.connect(self.make_ctime)
        self.id_result_button_2.clicked.connect(self.jisuan)
        self.id_result_next_button.clicked.connect(self.jisuan_next)


        # 设置定时器
        self.timer_time = QTimer(self)
        self.timer_time.timeout.connect(self.update_time_display)
        self.timer_time.start(1000)

        self.timer_count = QTimer(self)
        self.timer_count.timeout.connect(self.count_retime)
        self.timer_count.start(1000)

        # 连接按钮信号 设置屏幕伽马值
        self.bt_on_gama.clicked.connect(lambda: self.handle_gamma_ramp(lambda: mirFun.set_current_gamma_ramp(red=2.0, green=2.0, blue=2.0)))
        self.bt_off_gama.clicked.connect(lambda: self.handle_gamma_ramp(lambda: mirFun.set_current_gamma_ramp(red=1.0, green=1.0, blue=1.0)))


        # 连接按钮信号 打开网页
        self.map_all.clicked.connect(self.openPic)  # type: ignore
        self.map_biqi.clicked.connect(self.openPic)  # type: ignore
        self.map_wm.clicked.connect(self.openPic)  # type: ignore
        self.map_wgd.clicked.connect(self.openPic)  # type: ignore
        self.map_smz.clicked.connect(self.openPic)  # type: ignore
        self.map_zm.clicked.connect(self.openPic)  # type: ignore
        self.map_cyxg.clicked.connect(self.openPic)  # type: ignore
        self.map_zones_andian.clicked.connect(self.openPic)  # type: ignore
        self.map_zones_jiangshi.clicked.connect(self.openPic)  # type: ignore
        self.map_zones_wugong.clicked.connect(self.openPic)  # type: ignore
        self.map_zones_duojiao.clicked.connect(self.openPic)  # type: ignore
        self.map_zones_shouren.clicked.connect(self.openPic)  # type: ignore
        self.map_zones_woma.clicked.connect(self.openPic)  # type: ignore
        self.map_zones_shimu.clicked.connect(self.openPic)  # type: ignore
        self.map_zones_zm.clicked.connect(self.openPic)  # type: ignore
        self.map_zones_chiyue.clicked.connect(self.openPic)  # type: ignore
        self.map_zones_kulou.clicked.connect(self.openPic)  # type: ignore
        self.index.clicked.connect(self.openPic)  # type: ignore
        self.initsound()

        # 创建网络访问管理器
        self.net_manager = QNetworkAccessManager()
        self.net_manager.finished.connect(self.on_image_loaded)

        # 加载图片
        self.load_image()
        self.make_ctime()

    def handle_gamma_ramp(self, func):
        try:
            func()  # 执行传入的函数
        except Exception as e:
            # 将异常信息写入当前目录的 log.txt 文件
            with open("log.txt", "a") as log_file:
                log_file.write(f"Error: {str(e)}\n")
            print(f"捕获到异常: {str(e)}")  # 可选：控制台输出异常信息

    def load_image(self):
        url = QUrl()
        url.setUrl("http://cd7.okayapi.com/C9D0523F019B3D49CF0D62F5CDCDF60F_20250625114022_d0d39942a1e08614ef7b6578e87ec9fe.png")
        request = QNetworkRequest()
        request.setUrl(url)
        self.net_manager.get(request)


    def on_image_loaded(self, reply):
        # 检查是否有错误
        if reply.error():
            print("Error loading image:", reply.errorString())
            return

        # 读取图片数据
        data = reply.readAll()
        pixmap = QPixmap()
        pixmap.loadFromData(data)

        # 设置图片到 QLabel
        self.redbag.setPixmap(pixmap)
        self.redbag.setScaledContents(True)  # 如果需要缩放图片适应 QLabel

        # 调整窗口大小为图片大小
        self.resize(pixmap.width(), pixmap.height())
    def make_ctime(self):
        """记录当前时间"""
        current_time = self.getDate()
        self.id_tv_time.setText(current_time)
        self.re_time = current_time

    def getDate(self):
        """获取当前时间字符串"""
        return QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")

    def getDate2(self, dt):
        """格式化时间字符串"""
        return dt.toString("yyyy-MM-dd HH:mm:ss")

    def getmaptime(self):
        """获取地图刷新间隔时间（毫秒）"""
        if self.radioButton505.isChecked():
            return 505 * 1000
        elif self.radioButton1005.isChecked():
            return 1005 * 1000
        elif self.radioButton1505.isChecked():
            return 1505 * 1000
        else:  # 自定义
            try:
                sec = int(self.custom_time.text())
                return sec * 1000
            except ValueError:

                return 0

    def jisuan(self):
        """计算下次刷新时间"""
        try:
            result = calculate_refresh_time(self)
            self.re_time = self.id_tv_time.text()
            self.result.setText(result['str'])
            copy_to_clipboard(result['str'])
        except Exception as e:
            print("Error in jisuan:", e)
            import traceback
            traceback.print_exc()

    def jisuan_next(self):
        """已刷新后计算下次时间"""
        update_refresh_time(self)
        self.jisuan()

    def count_retime(self):
        """倒计时更新显示"""
        try:
            if not self.re_time:
                return

            rtime = QDateTime.fromString(self.re_time, "yyyy-MM-dd HH:mm:ss")
            if not rtime.isValid():
                return

            interval = self.getmaptime()
            rtime = rtime.addMSecs(interval)

            current_time = QDateTime.currentDateTime()
            ctime = (rtime.toMSecsSinceEpoch() - current_time.toMSecsSinceEpoch() - 2000) / 1000

            result_str = f"下次刷新时间约为{self.getDate2(rtime)}距离刷新还有{int(ctime)}秒"
            self.result.setText(result_str)

            # 背景闪烁效果
            if -10 < ctime <= 15:
                if self.isRed:
                    self.setStyleSheet("background-color: white;")
                else:
                    self.setStyleSheet("background-color: red;")
                self.isRed = not self.isRed
            else:
                self.setStyleSheet("")  # 恢复默认背景
        except Exception as e:
            print("Error in count_retime:", e)
            import traceback
            traceback.print_exc()

    def update_time_display(self):
        """更新时间显示"""
        self.tv_current_time.setText("格式:" + self.getDate())

    def update_status_label(self, text):
        """基础功能页-更新状态标签文本"""
        self.label_2.setText(f"<html><head/><body><p><span style=\" color:#55aaff;\">{text}</span></p></body></html>")


    def openPic(self):
        """
        打开触发控件对应的网页链接。
        使用系统默认浏览器打开 URL，格式为 https://mir2.malafish.cn/{id}
        """
        sender = self.sender()
        if not sender:
            return

        map_id = sender.objectName()  # 获取触发信号的控件 ID
        url = f"https://mir2.malafish.cn/{map_id}"
        webbrowser.open(url)  # 使用系统默认浏览器打开网页

    def initsound(self):

        # 初始化cb的状态,读取文件的md5值和名称来实现。
        # 查询到所有的group_sound中的checkbox，并调用switch_handler方法
        cbs = self.group_sound.findChildren(QCheckBox)
        for checkbox in cbs:
            if isinstance(checkbox, QCheckBox):
                # 分割名称,通过名称来判断功能并用不同的判断处理方法
                names = checkbox.objectName().split("_")
                self.switch_handler(names, checkbox)


    def switch_handler(self, nams, checkbox):
        """
        根据 nams[2] 的值执行不同的操作。
        :param nams: 包含操作类型的列表
        """
        if len(nams) < 3:
            print("参数不足，无法处理")
            return

        action = nams[1]

        match action:
            case "shutup":
                self.handle_shutup(nams[3], checkbox)
            case "prompt":
                self.handle_prompt(nams[3], checkbox)
            case _:
                print(f"未知的操作类型: {action}")


    def handle_shutup(self, sound_num, checkbox):
        """
        处理初始化：静音相关逻辑  根据文件名判断是否静音
        """
        if checkshutup(sound_num):
            checkbox.setChecked(True)
        checkbox.clicked.connect(lambda: self.shutup_checkbox(sound_num, checkbox))

    def shutup_checkbox(self, sound_num, checkbox):
        """
        处理静音checkbox点击事件
        """
        if checkbox.isChecked():
            shutup(sound_num)
        else:
            shutup_recover(sound_num)

    def handle_prompt(self, sound_num, checkbox):
        """
        处理初始化：提示音播放相关逻辑  根据MD5值判断声音文件是否替换过
        """
        if checkprompt(sound_num):
            checkbox.setChecked(True)
        checkbox.clicked.connect(lambda: self.prompt_checkbox(sound_num, checkbox))

    def prompt_checkbox(self, sound_num, checkbox):
        """
        处理提示音checkbox点击事件
        """
        if checkbox.isChecked():
            start_prompt(sound_num)
        else:
            prompt_recover(sound_num)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 创建应用程序实例
    window = MainWindow()  # 创建主窗口实例
    window.show()  # 显示窗口
    sys.exit(app.exec_())  # 运行应用程序事件循环

