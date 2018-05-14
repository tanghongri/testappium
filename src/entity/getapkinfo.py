import sys
import os
from appium import webdriver
'''
测试APK使用
获取apk相关信息
'''


def PATH(p): return os.path.abspath(
    # Returns abs path relative to this file and not cwd
    os.path.join(os.path.dirname(__file__), p)
)


def PrintDriverInfo(driver):
    if driver.current_package:
        print('##### current_package #####')
        print(driver.current_package)
    if driver.current_activity:
        print('##### current_activity #####')
        print(driver.current_activity)
    if driver.context:
        print('##### context #####')
        print(driver.context)
    if driver.contexts:
        print('##### contexts #####')
        print(driver.contexts)
    if driver.page_source:
        print('##### page_source #####')
        print(driver.page_source)
        print(driver.page_source)


if __name__ == '__main__':
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.1'
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['app'] = PATH(
        '../apps/apk/dingding.apk'
    )
    '''
    appium server的错误信息会告诉你 appPackage 和 appActivity
    [ADB] Found package: 'com.alibaba.android.rimet' and
    fully qualified activity name : 'com.alibaba.android.rimet.biz.SlideActivity'
    '''
    desired_caps['appPackage'] = 'com.alibaba.android.rimet'
    desired_caps['appActivity'] = '.biz.SplashActivity'

    try:
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    except Exception as e:
        print(e)
        print('connect appium server fail')
        exit(-1)
    PrintDriverInfo(driver)
    driver.quit()
