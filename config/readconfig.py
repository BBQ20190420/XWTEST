import os
from configparser import ConfigParser


#获取当前目录
cur_path=os.path.dirname(os.path.relpath(__file__))
#获取配置文件路径
configpath=os.path.join(cur_path,'conf.ini')
config=ConfigParser()
config.read(configpath)

requrl=config.get('requrl','QAurl')
redirecturl=config.get('requrl','redirecturl')
notifyurl=config.get('requrl','notifyurl')
platformNo=config.get('QA',"platformNo")
realname1=config.get('USER','realname1')
phone1=config.get('USER','phone1')
idcardNo1=config.get('USER','idcardNo1')
bankcardNo1=config.get('USER','bankcardNo1')


mailhost=config.get('EMAIL','sendhost')
senduser=config.get('EMAIL','senduser')
sendpwd=config.get('EMAIL','sendpwd')
receiveuser1=config.get('EMAIL','receiveuser1')
receiveuser2=config.get('EMAIL','receiveuser2')
