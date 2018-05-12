import sys
import os
from appium import webdriver
# 测试使用指定目录
sys.path.append("../testappium/src")
from model import dealdevice


def PATH(p): return os.path.abspath(
    # Returns abs path relative to this file and not cwd
    os.path.join(os.path.dirname(__file__), p)
)


if __name__ == '__main__':
    bRet, device = dealdevice.GetTarDevice()
    if not bRet:
        exit(-1)

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.1'
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['app'] = PATH(
        '../apps/apk/dingding.apk'
    )
    # 将要测试app的安装包放到自己电脑上执行安装或启动，
    # 如果不是从安装开始，则不是必填项，可以由下面红色的两句直接启动
    desired_caps['appPackage'] = 'com.alibaba.android.rimet'
    desired_caps['appActivity'] = '.biz.SplashActivity'
    #desired_caps['appWaitActivity'] = 'com.alibaba.android.rimet'
    #desired_caps['unicodeKeyboard'] = True
    #desired_caps['resetKeyboard'] = True

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    print(driver.current_activity)
    print(driver.page_source)
    print(driver.contexts) 
 
    el = driver.find_element_by_accessibility_id(
        'com.alibaba.android.rimet:id/login_slide_btn')
    el.click()
    driver.quit()
