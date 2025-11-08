
import traceback
from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QApplication


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


def replace_numbers_to_chinese(text):
    """
    将文本中的数字转换为全角数字，并替换特定关键词
    """
    number_map = {
        '0': '０',
        '1': '１',
        '2': '２',
        '3': '３',
        '4': '４',
        '5': '５',
        '6': '６',
        '7': '７',
        '8': '８',
        '9': '９',
    }

    word_map = {
        '下次刷新时间约为': '刷新时间为',
        '距离刷新还有': '还有'
    }

    # 先替换汉字关键词
    replaced_text = text
    for key, value in word_map.items():
        replaced_text = replaced_text.replace(key, value)

    # 再替换数字为全角数字
    result = ''.join(number_map.get(char, char) for char in replaced_text)

    return result


def copy_to_clipboard(text):
    """复制文本到剪贴板"""
    clipboard = QApplication.clipboard()  # 获取系统剪贴板
    clipboard.setText(text)
    # QMessageBox.information(None, "复制成功", "内容已复制到剪贴板")


