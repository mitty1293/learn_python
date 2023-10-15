from job_and_mail import JobWorker, Mail, SomeMailer
from logging_mailer_proxy import LoggingMailerProxy, SomeLogger

# 処理の過程をメールする元々のコード
mailer_1 = SomeMailer()
job_worker_1 = JobWorker(mailer=mailer_1)
job_worker_1.process()

# job_and_mail.pyモジュールを変更せずにロギング処理を加えたコード
mailer_2 = SomeMailer()
logger = SomeLogger()
logging_mailer_proxy = LoggingMailerProxy(target=mailer_2, logger=logger)
job_worker_2 = JobWorker(mailer=logging_mailer_proxy)
job_worker_2.process()
