import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

"""
App password can be generated here
https://myaccount.google.com/apppasswords

Example:
mail = Mail('test subject', 'perryism@gmail.com', 'perryism@gmail.com')
mail.text("Hello world!")

with Gmail('perryism@gmail.com', os.environ['GMAIL_APP']) as g:
    g.send(mail)"""

class Mail:
    def __init__(self, subject, sender, receiver):
        outer = MIMEMultipart('alternative')
        outer['Subject'] = subject
        outer['From'] = sender
        outer['To'] = receiver
        self.outer = outer
        self.sender = sender
        self.receiver = receiver

    def text(self, text):
        part1 = MIMEText(text, 'plain')
        self.outer.attach(part1)

    def html(self, html):
        self.outer.attach(MIMEText(html, 'html'))

    def add_attachment(self, content, filename):
        msg = MIMEMultipart()
        msg.set_payload(content)
        msg.add_header('Content-Disposition', 'attachment', filename=filename)
        self.outer.attach(msg)

    def __str__(self):
        return self.outer.as_string()

class Gmail:
    @staticmethod
    def instance():
       if os.environ['GMAIL_APP'] is None:
            raise "GMAIL_APP is not found in enviroment"

       return Gmail(os.environ['GMAIL_APP'])

    def __init__(self, username, token):
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(username, token)

    def send(self, mail):
        self.server.sendmail(mail.sender, mail.receiver, str(mail))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._quit()

    def _quit(self):
        self.server.quit()


if __name__ == "__main__":
    mail = Mail('test subject', 'perryism@gmail.com', 'perryism@gmail.com')
    mail.text("Hello world!")

    with Gmail('perryism@gmail.com', os.environ['GMAIL_APP']) as g:
        g.send(mail)
