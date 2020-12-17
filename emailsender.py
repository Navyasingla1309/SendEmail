import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
html = Template(Path('send.html').read_text())


email = EmailMessage()
email['from'] = 'person1'
email['to'] = 'abc@gmail.com'
email['subject']= 'CONGRATULATIONS! YOU JUST WON $10000000 CASH'
email.set_content(html.substitute({'name': 'pmon'}),'html')

with smtplib.SMTP(host ='smtp.gmail.com', port =587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('def@email.com', '')
    smtp.send_message(email)
    print('DONE!')
