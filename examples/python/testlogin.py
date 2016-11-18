 #coding=utf-8

"""
Simple iOS tests, showing accessing elements and getting/setting text from them.
"""

import unittest
import os      
from random import randint
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep


class testLogin(unittest.TestCase):

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
                'autoAcceptAlerts':'true'
            })

    def testLogin(self):

        #关闭新人礼弹窗
        #sleep(30)   
        #try:
            #newUsr=self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAStaticText[1]')
            #self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAButton[3]').click
            #print('关闭弹窗')
        #except Exception as e:
            #pass 
        #else:
            #pass
       
        
        #点击个人
        els=self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATabBar[1]/UIAScrollView[1]/UIAImage[5]')
        action=TouchAction(self.driver)
        action.tap(els).perform()

        #点击账号输入框
        elsUsrname=self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATextField[1]')
        elsUsrname.send_keys('yanxuantest1999@163.com')
        #点击密码框，输入密码
        elsPassword=self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIASecureTextField[1]')
        elsPassword.send_keys('abc123')
        self.driver.hide_keyboard()
        #点击登录
        self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAButton[1]').click
        sleep(30)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testLogin)
    unittest.TextTestRunner(verbosity=2).run(suite)
