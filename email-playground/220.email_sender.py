import smtplib
from email.message import EmailMessage

r = 0

while r < 2:
    email = EmailMessage()
    email['from'] = 'Patryk Petryszen'
    email['to'] = 'p.petryszen@gmail.com'
    email['subject'] = 'Zobacz to'

    email.set_content('Kocham Cie bardzo mocno! :****')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('bambo803@gmail.com', 'Aniagagi5')
        smtp.send_message(email)
        print('all good, that worked')
    r +=1