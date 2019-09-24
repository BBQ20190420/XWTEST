import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from xwtest.config import readconfig
from xwtest.common.getlog import getLog

mailhost=readconfig.mailhost
senduser=readconfig.senduser
sendpwd=readconfig.sendpwd
receiveuser1=readconfig.receiveuser1
receiveuser2=readconfig.receiveuser2

mylog=getLog()


def sendEmail(sendfile,sendtime):
    receiver = [receiveuser1]
    # 创建一个带附件实例
    message = MIMEMultipart()
    #发件人名字
    message['from'] = Header('存管测试结果报告', 'utf-8')
    #收件人名字
    message['to'] = Header('查看报告', 'utf-8')
    #邮件标头
    message['subject'] = Header('测试报告', 'utf-8')
    # 邮件正文内容
    message.attach(MIMEText("测试报告内容", 'plain', 'utf-8'))
    # 构造附件
    att1 = MIMEText(open(sendfile,'rb').read(),'base64','utf-8')
    att1['Content-Type'] = 'application/octet-stream'
   # att1['Content-Disposition'] = 'attachment;filename=%s' % str("bqqtest.html").encode('utf-8')
    att1.add_header('Content-Disposition', 'attachment', filename=('gbk', '', f"xwtest{sendtime}.html") )

    message.attach(att1)
    try:
        smtp=smtplib.SMTP()
        smtp.connect(mailhost,25)
        smtp.login(senduser,sendpwd)
        smtp.sendmail(senduser,receiver,message.as_string())
        smtp.quit()
        print("邮件发送成功")
    except Exception as e:
        print("邮件发送异常")
        print(e)
        mylog.warning(Exception)
