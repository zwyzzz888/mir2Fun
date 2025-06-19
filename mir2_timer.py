
import traceback
from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QMessageBox, QApplication


def calculate_refresh_time(main_window):
    """计算刷新时间核心逻辑"""
    try:
        re_time = main_window.id_tv_time.text()
        rtime = QDateTime.fromString(re_time, "yyyy-MM-dd HH:mm:ss")

        if not rtime.isValid():
            # QMessageBox.warning(main_window, "时间格式错误", "请输入有效的时间格式: YYYY-MM-DD HH:mm:ss")
            main_window.id_tv_time.setText(main_window.getDate())

        interval = main_window.getmaptime()
        rtime = rtime.addMSecs(interval)

        current_time = QDateTime.currentDateTime()
        ctime = (rtime.toMSecsSinceEpoch() - current_time.toMSecsSinceEpoch() - 2000) / 1000

        result_str = f"下次刷新时间约为{main_window.getDate2(rtime)}距离刷新还有{int(ctime)}秒"
        return {'rtime': rtime, 'str': result_str,'ctime': ctime}
    except Exception as e:
        print("Error in calculate_refresh_time:", e)
        traceback.print_exc()
        return {'rtime': QDateTime.currentDateTime(), 'str': '发生错误', 'ctime': 0}


def update_refresh_time(main_window):
    """更新记录的时间为下次刷新时间"""
    try:
        result = calculate_refresh_time(main_window)
        if result['ctime'] <= 0:
            main_window.id_tv_time.setText(main_window.getDate2(result['rtime']))
    except Exception as e:
        print("Error in update_refresh_time:", e)
        traceback.print_exc()


def copy_to_clipboard(text):
    """复制文本到剪贴板"""
    clipboard = QApplication.clipboard()  # 获取系统剪贴板
    clipboard.setText(text)
    # QMessageBox.information(None, "复制成功", "内容已复制到剪贴板")


