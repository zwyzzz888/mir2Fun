import os
import hashlib
from config import SOUND_MD5_LIST  # 导入 SOUND_MD5_LIST
import shutil  # 导入shutil模块用于文件复制

mir2FunWav_dir = os.path.join(os.getcwd(), 'Wav', 'mir2FunWav')  # 获取 Wav/mir2FunWav 目录路径
wav_dir = os.path.join(os.getcwd(), 'Wav')  # 获取 Wav 目录路径


def shutup(sound_num):
    """
    传入 sound_num 参数，在 Wav 目录下找到 sound_num-2.wav 和 sound_num-3.wav 文件，
    并将它们重命名为 sound_num-2.wav_bak 和 sound_num-3.wav_bak。
    :param sound_num: 声音编号
    """
    # 定义要处理的文件名
    files_to_rename = [
        f"{sound_num}-2.wav",
        f"{sound_num}-3.wav"
    ]
    
    # 遍历文件列表并进行重命名操作
    for file in files_to_rename:
        try:
            original_path = os.path.join(wav_dir, file)
            backup_path = os.path.join(wav_dir, f"{file}_bak")

            if os.path.exists(original_path):  # 检查文件是否存在
                os.rename(original_path, backup_path)  # 重命名为 .bak 文件
                print(f"已将 {original_path} 重命名为 {backup_path}")
            else:
                print(f"文件 {original_path} 不存在，跳过重命名")
        except Exception as e:
            print(e)
            pass


def shutup_recover(sound_num):
    """
    传入 sound_num 参数，在 Wav 目录下找到 sound_num-2.wav_bak 和 sound_num-3.wav_bak 文件，
    并将它们重命名为 sound_num-2.wav 和 sound_num-3.wav。
    :param sound_num: 声音编号
    """
    # 定义要恢复的文件名
    files_to_restore = [
        f"{sound_num}-2.wav_bak",
        f"{sound_num}-3.wav_bak"
    ]
    
    # 遍历文件列表并进行恢复操作
    for file in files_to_restore:
        try:
            print("shutup_recover  "+wav_dir +"   "+ file)
            backup_path = os.path.join(wav_dir, file)
            original_path = os.path.join(wav_dir, file[:-4])  # 移除 .bak 后缀
            print("backup_path:"+backup_path)
            print("original_path"+original_path)
            if os.path.exists(backup_path):  # 检查备份文件是否存在
                os.rename(backup_path, original_path)  # 恢复为原始文件名
                print(f"已将 {backup_path} 恢复为 {original_path}")
            else:
                print(f"文件 {backup_path} 不存在，跳过恢复")
        except Exception as e:
            print(e)
            pass


def checkshutup(sound_num):
    """
    检查在 Wav 目录下是否存在 sound_num-2.wav_bak 文件，
    并且 sound_num-2.wav 文件不存在。
    
    :param sound_num: 声音编号
    :return: 如果条件满足返回 True，否则返回 False
    """
    bak_file = f"{sound_num}-2.wav_bak"
    original_file = f"{sound_num}-2.wav"
    
    bak_path = os.path.join(wav_dir, bak_file)
    original_path = os.path.join(wav_dir, original_file)
    
    return os.path.exists(bak_path) and not os.path.exists(original_path)


def calculate_md5(file_path):
    """
    计算文件的 MD5 值。
    
    :param file_path: 文件路径
    :return: 文件的 MD5 值（字符串形式）
    """
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def get_config_md5(sound_num):
    """
    从 config.py 的 SOUND_MD5_LIST 中获取指定 sound_num 的 MD5 值。

    :param sound_num: 声音编号
    :return: 配置文件中的 MD5 值
    :raises KeyError: 如果配置文件中没有对应的 sound_num
    """
    try:
        return SOUND_MD5_LIST[sound_num]
    except KeyError:
        raise KeyError(f"配置文件中未找到 sound_num: {sound_num} 对应的 MD5 值。")


def checkprompt(sound_num):
    """
    检查 sound_num-1.wav 文件的 MD5 值是否与配置文件中的 MD5 值相等。
    
    :param sound_num: 声音编号
    :return: 如果 MD5 值相等返回 True，否则返回 False
    """
    wav_file = f"{sound_num}-1.wav"
    wav_path = os.path.join(wav_dir, wav_file)
    
    # 检查文件是否存在
    if not os.path.exists(wav_path):
        print(f"文件 {wav_path} 不存在")
        return False
    
    # 计算文件的 MD5 值
    print("wav_path="+wav_path)
    file_md5 = calculate_md5(wav_path)
    
    # 假设配置文件中存储了 sound_num 的 MD5 值
    config_md5 = get_config_md5(sound_num)  # 需要实现获取配置文件 MD5 的方法

    print("sound_num="+sound_num)
    print("file_md5="+file_md5)
    print("config_md5="+config_md5)

    # 对比 MD5 值
    return file_md5 == config_md5


def start_prompt(sound_num):
    """
    入参为 sound_num，先修改 Wav 目录下的 sound_num-1.wav 文件名改为 sound_num-1.wav_bak，
    然后把 mir2FunWav_dir 目录下的 sound_num-1.wav 复制到 Wav 目录中。

    :param sound_num: 声音编号
    """
    # 定义原始文件和备份文件的路径
    original_file = f"{sound_num}-1.wav"
    backup_file = f"{sound_num}-1.wav_bak"

    wav_original_path = os.path.join(wav_dir, original_file)
    wav_backup_path = os.path.join(wav_dir, backup_file)
    mir2FunWav_source_path = os.path.join(mir2FunWav_dir, original_file)

    # 检查原始文件是否存在并进行重命名操作
    if os.path.exists(wav_original_path):
        os.rename(wav_original_path, wav_backup_path)
        print(f"已将 {wav_original_path} 重命名为 {wav_backup_path}")
    else:
        print(f"文件 {wav_original_path} 不存在，跳过重命名")

    # 检查源文件是否存在并进行复制操作
    if os.path.exists(mir2FunWav_source_path):
        shutil.copy(mir2FunWav_source_path, wav_dir)
        print(f"已将 {mir2FunWav_source_path} 复制到 {wav_dir}")
    else:
        print(f"文件 {mir2FunWav_source_path} 不存在，跳过复制")


def prompt_recover(sound_num):
    """
    入参为 sound_num，先判断 sound_num-1.wav_bak 是否存在，
    然后删除 Wav 目录下的 sound_num-1.wav 文件（如果存在），
    最后将 sound_num-1.wav_bak 修改为 sound_num-1.wav。

    :param sound_num: 声音编号
    """
    # 定义备份文件和原始文件的路径
    backup_file = f"{sound_num}-1.wav_bak"
    original_file = f"{sound_num}-1.wav"

    wav_backup_path = os.path.join(wav_dir, backup_file)
    wav_original_path = os.path.join(wav_dir, original_file)

    # 检查备份文件是否存在
    if not os.path.exists(wav_backup_path):
        print(f"文件 {wav_backup_path} 不存在，无法恢复")
        return

    # 删除原始文件（如果存在）
    if os.path.exists(wav_original_path):
        os.remove(wav_original_path)
        print(f"已删除 {wav_original_path}")

    # 将备份文件重命名为原始文件名
    os.rename(wav_backup_path, wav_original_path)
    print(f"已将 {wav_backup_path} 恢复为 {wav_original_path}")
