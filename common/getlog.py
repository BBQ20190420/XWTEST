import logging
from logging.handlers import TimedRotatingFileHandler
import os
import time

def getLog():
    #获取log
    logger=logging.getLogger()
    #设置级别
    logger.setLevel(logging.ERROR)
    #设置格式
    format_log=logging.Formatter('%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    #输出到控制台
    screen_put=logging.StreamHandler()
    screen_put.setFormatter(format_log)
    #输出到文件
    log_path=os.path.join(os.getcwd(),'log')
    mytime=time.strftime('%Y%m%d%H',time.localtime(time.time()))
    # file_put=logging.FileHandler(os.path.join(log_path,'%s.log')%mytime,encoding='utf-8')
    #日志切割,when表示单位，interval表示几个单位，backupCount保留几个文件
    file_put=TimedRotatingFileHandler(os.path.join(log_path,'%s.log')%mytime,when='h',interval=1,backupCount=3,encoding='utf-8')
    file_put.setFormatter(format_log)
    #添加到handle
    logger.addHandler(screen_put)
    logger.addHandler(file_put)
    return logger
