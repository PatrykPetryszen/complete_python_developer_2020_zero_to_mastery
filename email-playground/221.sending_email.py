import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path #similar to os.path, it allows us to access html file

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Patryk Petryszen'
email['to'] = '[p.petryszen@gmail.com]'
email['subject'] = 'Zobacz to'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('bambo803@gmail.com', 'Aniagagi5')
    smtp.send_message(email)
    print('all good, that worked')