# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QButtonGroup

from uioutput import Ui_MainWindow
from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QClipboard

# 导入时间模块
from mir2_timer import calculate_refresh_time, update_refresh_time, copy_to_clipboard

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        global main_window_instance
        main_window_instance = self
        super(MainWindow, self).__init__(parent)
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
                QMessageBox.warning(self, "输入错误", "请输入有效的秒数")
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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 创建应用程序实例
    window = MainWindow()  # 创建主窗口实例
    window.show()  # 显示窗口
    sys.exit(app.exec_())  # 运行应用程序事件循环

