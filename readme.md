#更新requirements.txt为python313的各个版本的依赖

main.ui qt designer 界面文件
uioutput.py:main.ui 通过 pyuic5 -o uioutput.py main.ui生成的布局文件
mainUI.py: 继承uioutput界面逻辑文件,用于启动自定义逻辑,信号绑定槽方法


#  打包编译exe
## 方式一：pyinstaller  -F -w --version-file my.txt -i favicon.ico --noconsole --onefile .\mainRun.py --upx-dir D:\pyWorkspace\upx-3.96-win64\ --add-data "favicon.ico;." 
### 替换自己的upx目录  -w 有窗体，---noconsole 运行时无console，--console 运行时有console 
## 方式二：pyinstaller mainFun.spec  编辑spec文件 进行打包


尝试使用Nuitka打包
python -m nuitka --msvc=latest --standalone --onefile --windows-console-mode=disable --windows-icon-from-ico=favicon.ico  --output-dir=dist --include-module=requests --include-module=win32gui --enable-plugin=pyqt5  --enable-plugin=numpy --include-module=PyQt5 --include-module=PyQt5.QtWidgets --include-module=PyQt5.QtGui --include-module=PyQt5.QtCore --include-data-files=favicon.ico=favicon.ico --company-name="malafish" --product-name="malafish-tools" --file-description="malafish-tools" --file-version=1.1.1 --product-version=1.1.1 --copyright="malafish" --trademarks="malafish" mainRun.py


python -m nuitka --msvc=latest --standalone --onefile  --windows-icon-from-ico=favicon.ico  --output-dir=dist --include-module=requests --include-module=win32gui --enable-plugin=pyqt5  --enable-plugin=numpy --include-module=PyQt5 --include-module=PyQt5.QtWidgets --include-module=PyQt5.QtGui --include-module=PyQt5.QtCore --include-data-files=favicon.ico=favicon.ico --company-name="malafish" --product-name="malafish-tools" --file-description="malafish-tools" --file-version=1.1.0 --product-version=1.1.0 --copyright="malafish" --trademarks="malafish" mainRun.py


## 实现原理
### win32gui 操作窗口模拟键鼠操作，使用图片识别，判断状态

### 以下功能都是模拟键鼠操作，不影响游戏平衡性
### 使用方法介绍：
    先启动游戏，在窗口激活的状态下，alt + f12 初始化窗口，只适合1024 分辨率 未适配 800分辨率
    如果多开，就依次开游戏再依次启动多个本程序，使用快捷键时候，保证游戏窗口激活再按功能快捷键
    alt + esc 自动显示物品，拾取物品，其实就是不停的按esc，如果组队的时候需要临时关闭，再按次就关闭，以下同理
    alt + f1-7  自动训练技能，鼠标指向需要释放的地方，按下即可，再按停止，只能适合诱惑等技能，不适合道士需要换符的技能
    alt + f8  (启动时窗口需要在前台)自动训练道士换符技能，同上技能设置为f8，打开包裹，包裹里面装好符
    alt + m  快速卖、存、修 物品： 点开卖、修、仓库保管窗口后，鼠标指向物品 按快捷键即可 (启动时窗口需要在前台)
    alt + b  快速交易：打开交易窗口后，鼠标指向物品 按快捷键即可 (启动时窗口需要在前台)
    alt + f10 随机行走(可以后台)
    