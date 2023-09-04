"""
1. NotificationService という抽象クラスが導入され、それを継承する具象クラス EmailSender がメール送信の具体的な実装を提供します。
2. OrderProcessor クラスのコンストラクタに NotificationService インスタンスを受け取るように変更され、依存関係を注入するようになりました。

これにより、OrderProcessor は具体的なメール送信の詳細に依存せず、代わりに抽象的な通知サービスに依存するようになりました。
依存関係逆転原則を守ることで、将来的に他の通知サービスを簡単に統合でき、システムの柔軟性と保守性が向上します。
"""

from abc import ABC, abstractmethod


class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass


class EmailSender(NotificationService):
    def send_notification(self, message):
        # 具体的なメール送信の実装
        pass


class OrderProcessor:
    def __init__(self, notification_service):
        self.notification_service = notification_service

    def process_order(self, order):
        # 注文の処理
        message = f"注文が受け付けられました。注文番号: {order.order_number}"
        self.notification_service.send_notification(message)
