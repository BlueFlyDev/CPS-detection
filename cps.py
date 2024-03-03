from pynput import mouse
import time

# 全局变量用于存储上一次点击的时间和当前CPS限制
last_click_time = 0
cps_limit = 0

def on_click(x, y, button, pressed):
    global last_click_time
    if pressed:
        # 计算两次点击之间的间隔
        current_time = time.time()
        interval = current_time - last_click_time

        # 如果间隔小于CPS对应的时间间隔，则忽略此次点击
        if interval < 1 / cps_limit:
            print("点击过快，此次点击被忽略")
            # 不再返回False，以免停止监听器

        # 更新上一次点击的时间
        last_click_time = current_time

def main():
    global cps_limit

    # 让用户输入CPS限制
    cps_limit = float(input("请输入你想要限制的CPS: "))

    # 使用鼠标监听器监听点击事件
    listener = mouse.Listener(on_click=on_click)
    listener.start()  # 启动监听器，但不阻塞当前线程
    print("CPS限制开启退出直接关闭")

    # 无限循环，直到用户强制退出
    try:
        while True:
            time.sleep(10)  # 仅作为示例，减少CPU使用率
    except KeyboardInterrupt:
        listener.stop()  # 如果用户强制退出，停止监听器

if __name__ == "__main__":
    main()
