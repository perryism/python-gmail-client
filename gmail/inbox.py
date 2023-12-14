# get the latest email from gmail inbox

import imaplib
from .received_email import ReceivedEmail

class Inbox:
    def __init__(self, email, passwd):
        self.email = email
        self.passwd = passwd
        self.mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
        self.mail.login(self.email, self.passwd)
        self.mail.select('INBOX')

    def get_latest_email(self, per_page=50):
        result, data = self.mail.uid("search", None, "ALL")
        i = len(data[0].split()) - 1
        for x in range(i, 0, -1):
            latest_email_uid = data[0].split()[x]
            result, email_data = self.mail.uid("fetch", latest_email_uid, "(RFC822)")
            email = ReceivedEmail.from_email_message(email_data)
            yield email

if __name__ == "__main__":
    import os
    inbox = Inbox("perryism@gmail.com", os.environ['GMAIL_APP'])

    for i, eml in enumerate(inbox.get_latest_email()):
        if "perryism@gmail.com" in eml.sender:
            print(eml.sender, eml.subject, eml.date, eml.body)

        if i == 50:
            break
