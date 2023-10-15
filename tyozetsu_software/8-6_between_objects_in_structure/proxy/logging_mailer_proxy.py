from abc import ABC, abstractmethod

from job_worker import MailerInterface


class LoggerInterface(ABC):
    @abstractmethod
    def info(self, message: str):
        pass


class SomeLogger(LoggerInterface):
    def info(self, message: str):
        print(message)


class LoggingMailerProxy(MailerInterface):
    def __init__(self, target: MailerInterface, logger: LoggerInterface):
        self.target = target
        self.logger = logger

    def send(self, mail):
        self.logger.info(f"Before send {mail.address}")
        self.target.send(mail)
        self.logger.info(f"After send {mail.address}")
