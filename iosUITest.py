# coding=utf-8

import os
from time import sleep

from appium.webdriver import webdriver
from appium import webdriver
import startAppium


class iosUITest:
    def setUp(self):
        # set up appium
        app = os.path.abspath('../../apps/TestYanXuan/build/debug-iphonesimulator/NeteaseYanxuan.app')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '9.3',
                'deviceName': 'iPhone 6',
                'autoAcceptAlerts': 'true'
            })
        #self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[4]/UIAButton[1]').click()

    def tearDown(self):
            self.driver.quit()

if __name__ == '__main__':
    iosUITestCase = iosUITest()
    # 启动appium服务
    startAppium.startappium()
    # 启动xcode模拟器
    iosUITestCase.setUp()
    sleep(100)
    iosUITestCase.tearDown()
