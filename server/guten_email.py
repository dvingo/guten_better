
import smtplib

def send_guten_email(recipient, day, chunk):
    user = u'gutenbetter@gmail.com'
    password = '' # TODO: fill in password, don't commit to git ;)
    subject = u'Guten Better Day ' + str(day)

    # TODO: html baby... html
    body = 'Enjoy!!! Guten Better Day {0} Baby...\n\n{1}'.format(day, chunk)

    send_email(user, password, recipient, subject, body)

# lol http://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python
def send_email(user, pwd, recipient, subject, body):

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = '\From: {0}\nTo: {1}\nSubject: {2}\n\n{3}'.format(FROM, ', '.join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except Exception, e:
        print "failed to send mail: ", e
