import sys
import os
from appium import webdriver
# 测试使用指定目录
sys.path.append("../testappium/src")
from entity import getapkinfo


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
    desired_caps['noReset'] = True

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    el = driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.alibaba.android.rimet:id/home_bottom_tab_button_work")')
    el.click()

    el = driver.find_element_by_android_uiautomator('new UiSelector().text("考勤打卡")')
    el.click()

    #el = driver.find_element_by_android_uiautomator("com.alibaba.android.rimet:id/et_phone_input").send_keys("13811894468")

    driver.quit()
