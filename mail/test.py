import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

msg = MIMEText('这是一封测试邮件','html','utf-8')
msg['Form'] = formataddr(['周艳宇','zhouyanyus@foxmail.com'])
msg['Subject'] = '这是一封测试邮件'

server = smtplib.SMTP_SSL('smtp.qq.com')
server.login('zhouyanyus@foxmail.com', 'xhhdrkrmmwqpbaic')
server.sendmail('zhouyanyus@foxmail.com', 'theyanyus@outlook.com', msg.as_string())
server.quit()