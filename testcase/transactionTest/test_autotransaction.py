import unittest
from xwtest.common.param import getRequestNo
from xwtest.common.extt import http
from xwtest.common.getnotify import getNotify
import json
import time
class Transaction(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass
    def test_marketing(self):
        """
        交易——发红包
        """
        myrequestNo=getRequestNo()
        mdreq = {
            "batchNo": "batch" + getRequestNo(),
            "bizDetails": [{
                "requestNo": myrequestNo,
                "tradeType": "MARKETING",
                "details": [
                    {
                        "bizType": "MARKETING",
                        "sourcePlatformUserNo": "SYS_GENERATE_002",
                        "targetPlatformUserNo": "autoIn01",
                        "amount": "0.01",
                        "customDefine": "2019028737"
                    }

                ]
            }]
        }


        resp=http.req_direct("ASYNC_TRANSACTION",mdreq)
        time.sleep(20)
        #llgetNotify(myrequestNo)
        self.assertEqual(resp['status'],"SUCCESS")


if __name__ == '__main__':
    unittest.main()