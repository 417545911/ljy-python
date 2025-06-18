import pyautogui

screenWidth,screenHeight = pyautogui.size()
currentMouseX,currentMouseY = pyautogui.position()

pyautogui.moveTo(100, 160)
pyautogui.click()

# Hello world1鼠标向下移动10像素
pyautogui.moveRel(None,10)
pyautogui.doubleClick()

# 用缓动/渐变函数让速表2秒后移动到（500，500）位置
# use tweening/easing function to move mouse over 1 seconds.
pyautogui.moveTo(300,190,duration=1,tween=pyautogui.easeInOutQuad)
pyautogui.click()
# 在每次输入之间暂停0.25秒
pyautogui.typewrite("Hello world!",interval=0.25)
pyautogui.press('esc')
pyautogui.keyDown('shift')
pyautogui.press(['left','left','left','left','left','left'])
pyautogui.keyUp('shift')
pyautogui.hotkey('command','c')
#  返回一个Pillow/PIL的Image对象
try:
    screenshot = pyautogui.screenshot()
    print("截图已创建")
    screenshot.save('./screenshots/foo.png')
    print("截图已保存到 ./screenshots/foo.png")
except Exception as e:
    print(f"截图失败: {str(e)}")