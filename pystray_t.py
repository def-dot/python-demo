# 系统托盘程序
# （1）创建系统托盘图标
# （2）监听系统托盘事件，如鼠标点击、右键

import pystray
from pystray import MenuItem as item
from PIL import Image

# 定义托盘图标
icon = Image.open("icon.png")

# 定义系统托盘菜单
menu = (item("Say Hello", lambda: print("Hello!")),
        item("Exit", lambda: pystray.stop()))


# 创建系统托盘图标
def create_tray_icon():
    tray_icon = pystray.Icon("hello", icon, "Hello", menu)
    tray_icon.run()


# 运行程序
if __name__ == "__main__":
    create_tray_icon()
