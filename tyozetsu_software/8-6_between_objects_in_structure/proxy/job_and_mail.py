from abc import ABC, abstractmethod


class Mail:
    def __init__(self):
        self.address = "some address"


class MailerInterface(ABC):
    @abstractmethod
    def send(self, mail: Mail):
        pass


class SomeMailer(MailerInterface):
    def send(self, mail: Mail):
        print(mail.address)


class JobWorker:
    def __init__(self, mailer: MailerInterface):
        self.mailer = mailer

    def process(self):
        # ジョブを処理する
        report_mail = Mail()
        self.mailer.send(report_mail)
        # なにか後処理をする
