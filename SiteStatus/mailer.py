#!/usr/bin/python
import requests

cfg_file = "config.ini"
replyto = "kotek.vojtech@gmail.com"

class mail(object):

    # Get mailgun config from file
    def __init__(self):
        import configparser
        cfg = configparser.RawConfigParser()
        cfg.read(cfg_file)
        mg = "mailgun" #section name
        self.api_key = cfg.get(mg, 'api_key')
        self.mg_from = cfg.get(mg, 'from_mail')

    # Send message
    def send(self, to, subject, body):
        return requests.post(
            "https://api.mailgun.net/v3/kotek.co/messages",
            auth=("api", self.api_key),
            data={
                "from": self.mg_from,
                "to": to,
                "subject": subject,
                "h:Reply-To": replyto,
                "html": body})

if __name__ == "__main__":
    m = mail()
    print(m.send(["kotek.vojtech@gmail.com"],"No Subject","Hello. this is a test"))
