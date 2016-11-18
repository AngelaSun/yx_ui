# coding=utf-8

"""
Simple iOS tests, showing accessing elements and getting/setting text from them.
"""

import unittest
import os
from random import randint
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep


class MemoryTest:
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

    def clickTopic(self):
        # 关闭升级弹窗
        self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[4]/UIAButton[1]').click()
        sleep(3)
        # 点击专题,进入专题列表页
        element = self.driver.find_element_by_xpath(
            '//UIAApplication[1]/UIAWindow[1]/UIATabBar[1]/UIAScrollView[1]/UIAImage[2]')
        act = TouchAction(self.driver)
        act.tap(element).perform()
        #进入专题,上滑翻到底部
        sleep(3)
        self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]').click()
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        #self.driver.swipe(start_x=width / 2, start_y=50, end_x=width / 2, end_y=500, duration=1000)
        elWebView = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]')
        act.press(elWebView, width / 2, height * 3/4).move_to(width / 2, height/4).release().perform()
        sleep(10)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = MemoryTest()
    suite.setUp()
    suite.clickTopic()
    suite.tearDown()
