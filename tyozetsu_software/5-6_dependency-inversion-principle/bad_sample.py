"""
OrderProcessor クラスが EmailSender クラスに直接依存しています。
これは依存関係逆転原則に反しており、問題が発生する可能性があります。
なぜなら、将来的にメール送信の方法を変更する必要が生じた場合、
OrderProcessor クラスに変更を加える必要があるためです。
"""


class EmailSender:
    def send_email(self, message):
        # 具体的なメール送信の実装
        pass


class OrderProcessor:
    def process_order(self, order):
        # 注文の処理
        email_sender = EmailSender()
        email_message = f"注文が受け付けられました。注文番号: {order.order_number}"
        email_sender.send_email(email_message)
