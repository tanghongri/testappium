import sys
import os
from appium import webdriver


def PATH(p): return os.path.abspath(
    # Returns abs path relative to this file and not cwd
    os.path.join(os.path.dirname(__file__), p)
)


if __name__ == '__main__':
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.1'
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['app'] = PATH(
        '../apps/apk/dingding.apk'
    )
    desired_caps['appPackage'] = 'com.alibaba.android.rimet'
    desired_caps['appActivity'] = '.biz.SplashActivity'

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    el = driver.find_element_by_android_uiautomator(
        'new UiSelector().className("android.widget.Button").instance(0)')
    el = driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.alibaba.android.rimet:id/login_slide_btn")')
    el = driver.find_element_by_android_uiautomator(
        'new UiSelector().text("新用户注册")')   
    el.click()
    driver.quit()
