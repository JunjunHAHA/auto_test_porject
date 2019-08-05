#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

def sendTestEmail(filename):
    user = "@qq.com"
    password = ""
    to_addrs = "@qq.com"
    
    #编辑邮件的内容
    #主题
    subject = "测试报告"
    #正文部分
    content = "第一封测试邮件"
    # msg = MIMEText(content)
    # msg['Subject'] = subject
    # msg['From'] = user
    # msg['To'] = to_addrs
    
    #添加了附件的邮件内容
    msg = MIMEMultipart()
    msg['From'] = Header('班主任', 'utf-8')  #在发件人的位置显示中文昵称
    msg['To'] = Header('同学', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg.attach(MIMEText(content, 'plain', 'utf-8'))  #将正文部分加入到msg中
    #添加附件的部分
    att = MIMEText(open("./%s.html" % filename, 'r').read(), "base64", "utf-8")
    att['Content-Type'] = 'application/actet-stream'
    att['Content-Disposition'] = 'attachment;filename="tester.html"'   #重新定义你的附件名称
    msg.attach(att)
    
    
    #使用smtplib模块发送邮件
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(user, password)
    s.sendmail(user, to_addrs, msg.as_string())  #自己的地址，发送给谁，邮件的内容
