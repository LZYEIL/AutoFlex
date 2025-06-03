from autoflex.core.web_manager import Browser
from autoflex.core.actions import Actions
from autoflex.core.exceptions import BrowserLaunchError
import time


def on_key_press(key):
    print(f"[监听] 键盘按下: {key}")
    if str(key) == "'q'":
        print("监听到 Q，停止监听")
        return False


def on_mouse_click(x, y, button, pressed):
    if pressed:
        print(f"[监听] 鼠标点击: ({x},{y}) {button}")


try:
    # 启动浏览器
    driver = Browser.start("edge")
    Actions.take_screenshot("startup.png")

    # 打开百度并执行点击+输入+截图
    driver.get("https://www.baidu.com")
    Actions.take_screenshot("baidu_home.png")
    Actions.click(locator=("css selector", "#kw"))
    Actions.type_text("AutoFlex 调度器测试")
    Actions.click(locator=("css selector", "#su"))

    # 鼠标移动+截图
    Actions.move_to(500, 200)
    Actions.take_screenshot("after_move.png")

    # 执行 Pynput 键盘监听
    print("按 Q 键停止键盘监听：")
    Actions.start_keyboard_listener(on_key_press)

    # 执行 Pynput 鼠标监听
    print("鼠标点击事件监听中，单击停止监听：")
    Actions.start_mouse_listener(on_mouse_click)

    input("测试完成，按 Enter 退出")
    Browser.quit()

except BrowserLaunchError as e:
    print(f"Failed to launch browser: {e}")
except Exception as e:
    print(f"执行异常: {e}")

