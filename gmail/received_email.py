from dataclasses import dataclass
import email

@dataclass
class ReceivedEmail:
    sender : str
    subject: str
    date: str
    body: str

    @classmethod
    def from_email_message(cls, email_data):
        raw_email = email_data[0][1]
        raw_email_string = raw_email.decode("utf-8")
        email_message = email.message_from_string(raw_email_string)
        date_tuple = email.utils.parsedate_tz(email_message["Date"])
        subject = email_message["Subject"]
        return cls(
            sender=email_message["From"],
            subject=subject,
            date=date_tuple,
            body=email_message.get_payload()
        )