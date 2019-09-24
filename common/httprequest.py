import requests
from xwtest.common.xwsign import rsaSign
from xwtest.common.param import getRequestNo,getTime
import json
from xwtest.config import readconfig
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
import execjs

reqUrl=readconfig.requrl
platformNo=readconfig.platformNo
redirectUrl=readconfig.redirecturl


class Httpreq():




    def reqBody(self,serviceName,reqData,*userDevice):


        '''封装请求格式'''
        sign=rsaSign(reqData)
        body = {
            "serviceName": serviceName,
            "platformNo": platformNo,
            "userDevice": userDevice,
            "reqData": reqData,
            "keySerial": "1",
            "sign": sign

        }

        return body


    def req_direct(self,serviceName,reqData,*userDevice):
        directurl=reqUrl+'/service'
        fixpara={
            # 'platformNo': platformNo,
            "timestamp":getTime()
        }
        fixpara.update(reqData)

        postdata=self.reqBody(serviceName,json.dumps(fixpara),*userDevice)
        print("请求是",postdata)

        resp=requests.post(directurl,data=postdata)
        print("请求结果是",resp.json())
        return resp.json()

    def req_gateway(self,serviceName,reqData,*userDevice):
        global callbacktoken
        callbacktoken=getRequestNo()
        gateurl=reqUrl+'/gateway'

        #无界面启动
        # option=Options()
        # option.add_argument('--headless')
        # driver=webdriver.Chrome(chrome_options=option)

        #有界面启动
        driver=webdriver.Chrome()


        fixpara = {
            'platformNo': platformNo,
            "timestamp": getTime(),
            'redirectUrl':redirectUrl+'request/'+callbacktoken
        }
        fixpara.update(reqData)
        req=json.dumps(fixpara)
        driver.get("about:blank")
        initform = """
               var html = '<form id="form" method="post" accept-charset="UTF-8">'
                + '<input id="serviceName" type="text" name="serviceName">'
                + '<input id="platformNo" type="text" name="platformNo">'
                + '<input id="reqData" type="text" name="reqData">'
                + '<input id="userDevice" type="text" name="userDevice">'
                + '<input id="sign" type="text" name="sign">'
                + '<input type="text" name="keySerial" value="1">'
                + '</form>'
               document.body.innerHTML = html;
               """
        driver.execute_script(initform)
        driver.find_element_by_id("serviceName").send_keys(serviceName)
        driver.find_element_by_id("platformNo").send_keys(platformNo)
        driver.find_element_by_id("reqData").send_keys(req)
        driver.find_element_by_id("userDevice").send_keys(userDevice)
        driver.find_element_by_id("sign").send_keys(rsaSign(req))

        js_form='document.getElementById("form").action="'+gateurl+"\""
        js_submit='document.getElementById("form").submit()'

        driver.execute_script(js_form)
        driver.execute_script(js_submit)

        postdata = self.reqBody(serviceName, json.dumps(fixpara), *userDevice)
        print("请求是", postdata)


        return driver

        # javascript(code)
        # $("#form").action = config().apiUrl + "gateway"
        # $("#serviceName").val(service)
        # $("#platformNo").val(config().platformNo_group)
        # $("#reqData").val(json)
        # $("#userDevice").val(userDevice)
        # $("#sign").val(doSign1(json))
        # $("#form").submit()


    def response(self):
        resp=requests.get(redirectUrl+'last/'+callbacktoken).json()['respData']
        print("返回结果",resp)
        return json.loads(resp)







