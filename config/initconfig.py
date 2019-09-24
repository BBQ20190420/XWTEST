from configparser import ConfigParser

config=ConfigParser()

config['requrl']={
    "QAurl":'http://172.19.60.92:8001/bha-neo-app/lanmaotech/',
    "redirecturl":"http://172.19.60.105:8090/lanmao-autotest-app/util/recorder/",
    'notifyurl':"http://172.19.60.105:9000/lanmao-autotest-app/findNotify.json"

}

config['QA']={
    'platformNo':'6000001510'
}

config['USER']={
    'realname1':"包倩倩",
    'phone1':'18101309652',
    'idcardNo1':'421302199410278443',
    'bankcardNo1':'6214830165885301',
    'realname2':"梁慧琳",
    'phone2':'18811165327',
    'idcardNo2':'131081198912141047',
    'bankcardNo2':'6214920206176743'
}

config['EMAIL']={
    'sendhost':'smtp.qq.com',
    'senduser':'1366441541@qq.com',
    'sendpwd':'zvqwxsunmfpehffd',
    'receiveuser1':'1280147527@qq.com',
    'receiveuser2':'qianqian.bao@lanmaoly.com'
}

with open('conf.ini','w') as file:
    config.write(file)