#  打包编译exe
## pyinstaller  -F -w --version-file my.txt -i .\bitbug_favicon.ico --console --onefile .\mainRun.py --upx-dir D:\pyWorkspace\upx-3.96-win64\
### 替换自己的upx目录

## 实现原理
### win32gui 操作窗口模拟键鼠操作，使用图片识别，判断状态

### 以下功能都是模拟键鼠操作，不影响游戏平衡性
### 使用方法介绍：
    先启动游戏，在窗口激活的状态下，alt + f12 初始化窗口，只适合1024 分辨率 未适配 800分辨率
    如果多开，就依次开游戏再依次启动多个本程序，使用快捷键时候，保证游戏窗口激活再按功能快捷键
    alt + esc 自动显示物品，拾取物品，其实就是不停的按esc，如果组队的时候需要临时关闭，再按次就关闭，以下同理
    alt + f7  自动训练技能，把技能设置为f7键释放，鼠标指向需要释放的地方，按下即可，再按停止，只能适合诱惑等技能，不适合道士需要换符的技能
    alt + f8  (启动时窗口需要在前台)自动训练道士换符技能，同上技能设置为f8，打开包裹，包裹里面装好符
    alt + m  (启动时窗口需要在前台)自动卖、存、修 物品， 点开卖、修、仓库保管窗口后，鼠标指向物品 按快捷键即可
    alt + f10 随机行走(可以后台)