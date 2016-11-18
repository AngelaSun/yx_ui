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


class SimpleIOSTests(unittest.TestCase):
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

    def test_buyNow(self):

        # 点击新品首发,进入新品首发
        #self.driver.find_element_by_accessibility_id('新品首发')
        self.driver.find_element_by_xpath(
            '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIATableView[1]/UIATableGroup[5]'
            '/UIAStaticText[1]').click()


        # 点击第一个商品,进入商品详情页
        self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]'
                                          '/UIAButton[1]').click()
        sleep(3)
        # 点击立即购买
        self.driver.find_element_by_accessibility_id('立即购买').click()
        # self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAButton[1]').click()

        # 未登录,需要登录
        # 点击账号输入框
        elsUsrname = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATextField[1]')
        elsUsrname.send_keys('yanxuantest1999@163.com')
        # 点击密码框，输入密码
        elsPassword = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIASecureTextField[1]')
        elsPassword.send_keys('abc123')
        self.driver.hide_keyboard()
        # 点击登录
        self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAButton[1]').click
        sleep(3)

        #判断是否需要选择规格
        try:
            self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]')
            # 选择第一个规格
            self.driver.find_element_by_xpath(
                '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAScrollView[1]/UIACollectionView[1]'
                '/UIACollectionCell[1]/UIAStaticText[1]').click()
            self.driver.find_element_by_accessibility_id('立即购买').click()
        except:
            pass

        # 进入下单页,点击结算
        sleep(3)
        self.driver.find_element_by_accessibility_id('结算').click()
        self.driver.find_element_by_accessibility_id('网易支付').click()
        sleep(10)
        # 输入支付密码
        payPsd=self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[2]/UIATableView[1]/UIATableCell[3]'
                                                 '/UIATextField[1]')
        payPsd.send_keys('111111')

        sleep(10)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
