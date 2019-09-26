import unittest
from xwtest.config import readconfig
from xwtest.common.extt import http
from xwtest.common.param import getRequestNo
from xwtest.common.getscreen import getScreen
import time
import os
import sys
import json
from selenium.webdriver import ActionChains

platformNo = readconfig.platformNo
realname1 = readconfig.realname1
phone1 = readconfig.phone1
idcardNo1 = readconfig.idcardNo1
bankcardNo1 = readconfig.bankcardNo1


class registerPersonal(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        self.thisdriver.quit()

    def test_Regiserp1(self):
        """
        注册流程——PC
        """
        requestNo = getRequestNo()
        req = {
            "platformUserNo": 'user' + requestNo,
            "requestNo": requestNo,
            "realName": realname1,
            "idCardType": 'PRC_ID',
            "userRole": 'INVESTOR',
            "idCardNo": idcardNo1,
            "mobile": phone1,
            "bankcardNo": bankcardNo1,
            "checkType": 'LIMIT',
            "expired": "20201210120000"
        }

        self.thisdriver = http.req_gateway("PERSONAL_REGISTER_EXPAND", req, "WEB")
        self.thisdriver.implicitly_wait(3)
        self.thisdriver.find_element_by_id("sendSmsVerify").click()
        time.sleep(2)
        #     #  thisdriver.find_element_by_xpath('//*[@id="alertLayer-2"]/div[2]/a').click()
        # element=thisdriver.find_element_by_xpath("//a[contains(text(),'我知道了')]")
        # ActionChains(thisdriver).move_to_element(element).perform()
        #
        # thisdriver.find_element_by_xpath("//a[contains(text(),'我知道了')][1]").click()

        self.thisdriver.find_element_by_class_name("submitBtn-2").click()
        time.sleep(5)
        self.thisdriver.find_element_by_id("smsCode").send_keys('888888')
        self.thisdriver.find_element_by_id("password").send_keys("123456")
        self.thisdriver.find_element_by_id("confirmPassword").send_keys("123456")
        self.thisdriver.find_element_by_id("isAgreeReg").click()
        self.thisdriver.find_element_by_id("nextButton").click()

        time.sleep(3)
        resp = http.response()
        self.assertEqual(resp['code'],"0")

    def test_Regiserp2(self):
        """
        注册流程——MOBILE
        """

        requestNo = getRequestNo()
        req = {
            "platformUserNo": 'user' + requestNo,
            "requestNo": requestNo,
            "realName": realname1,
            "idCardType": 'PRC_ID',
            "userRole": 'INVESTOR',
            "idCardNo": idcardNo1,
            "mobile": phone1,
            "bankcardNo": bankcardNo1,
            "checkType": 'LIMIT',
            "expired": "20201210120000"
        }

        self.thisdriver = http.req_gateway("PERSONAL_REGISTER_EXPAND", req, "MOBILE")
        self.thisdriver.implicitly_wait(3)

        try:

            self.thisdriver.find_element_by_id("sendSmsVerify").click()
            time.sleep(2)

            # #根目录
            # root_path=os.path.abspath(os.path.join(os.getcwd(),"../.."))
            # srceen_path = os.path.join(root_path, 'snapshot')
            # print(srceen_path)
            # nowtime = time.strftime("%Y%m%d.%H.%M.%S")
            # self.thisdriver.get_screenshot_as_file(srceen_path + "/" + "%s.png" % nowtime)
            #     #  thisdriver.find_element_by_xpath('//*[@id="alertLayer-2"]/div[2]/a').click()
            # element=thisdriver.find_element_by_xpath("//a[contains(text(),'我知道了')]")
            # ActionChains(thisdriver).move_to_element(element).perform()
            #
            #self.thisdriver.find_element_by_xpath("//a[@class='submit-btn']").click()
            #self.thisdriver.find_element_by_xpath("//form[@id='kw' and @name='wd']").send_keys("python")
            eles=self.thisdriver.find_elements_by_xpath("//a[contains(text(),'知道了')]")
            for i in eles:
                if i.get_attribute('class')=='blue':
                    i.click()

            #self.thisdriver.switch_to_alert
            # #eles=self.thisdriver.find_elements_by_class_name('submit-btn')
            # #print(eles)
            # #self.thisdriver.find_elements_by_xpath(('./div[@class="blue"]'))
            # eles=self.thisdriver.find_elements_by_class_name("submit-btn")
            # print(eles)
            # print(len(eles))
            # for i in eles:
            #     print(i.get_attribute("class"))
            time.sleep(2)
            self.thisdriver.find_element_by_id("smsCode").send_keys('888888')
            self.thisdriver.find_element_by_id("password").send_keys("123456")
            self.thisdriver.find_element_by_id("confirmPassword").send_keys("1234561")
            self.thisdriver.find_element_by_id("isAgreeReg").click()
            self.thisdriver.find_element_by_id("nextButton").click()



            # time.sleep(3)
            # resp = http.response()
        #     # self.assertEqual(resp['code'], "0")
        except Exception:
            function_name = sys._getframe().f_code.co_name

            getScreen(self.thisdriver,function_name)

        finally:
            resp = http.response()
            self.assertEqual(resp['code'], "0")


if __name__ == '__main__':
        unittest.main()