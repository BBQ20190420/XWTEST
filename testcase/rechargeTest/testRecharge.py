import unittest
from xwtest.common.param import getRequestNo
from xwtest.common.extt import http
class Recharge(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_autorecharge(self):
        """自动充值"""
        req={
            "platformUserNo":"autoBo01",
            "requestNo":getRequestNo(),
            "amount":1,
            "commission":0.01,
            "expectPayCompany":"ALLINPAY",
            "rechargeWay":"PROXY",
            "bankcode":"CMBC"

        }
        resp=http.req_direct(serviceName="DIRECT_RECHARGE",reqData=req)
        self.assertEqual(resp['rechargeStatus'],"SUCCESS")
if __name__ == '__main__':
    unittest.main()