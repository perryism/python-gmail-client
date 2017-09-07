import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

"""
App password can be generated here
https://myaccount.google.com/apppasswords

Example:
e = Gmail('subject', receiver, sender)
e.text("This is a text body")
e.html("<h1>This is a html body</h1>")
e.add_attachment(html, "result.html")
e.add_attachment(html, "result2.html")
e.send()
"""
class Gmail:
    def __init__(self, subject, receiver, sender):
        if os.environ['GMAIL_APP'] is None:
            raise "GMAIL_APP is not found in enviroment"

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

    def send(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.sender, os.environ['GMAIL_APP'])

        server.sendmail(self.sender, self.receiver, self.outer.as_string())
        server.quit()
