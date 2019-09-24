import requests
from xwtest.config import readconfig
import json
import time
notifyUrl=readconfig.notifyurl


def getNotify(requestNo):
    print(requestNo)
    # resp = requests.post(notifyUrl, requestNo)
    for i in range(100):
        resp = requests.get(notifyUrl, requestNo)
        print(i,resp.json())
        time.sleep(3)
        resp1 = requests.post(notifyUrl, requestNo)
        print(i,resp1.json())


    # print(resp.json())


