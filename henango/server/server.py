import socket

from henango.server.worker import Worker

class Server:
	"""
	Webサーバーを表すクラス
	"""

	def serve(self):
		"""
		サーバーを起動するメソッド
		"""
		print("===サーバーを起動します===")
		
		try:
			# socket生成
			server_socket = self.create_server_socket()

			while True:
				# accept: 接続を待ち、接続があればコネクションを確立する
				print("=== Server: クライアントからの接続を待ちます===")
				(client_socket, address) = server_socket.accept()
				# 確立後、返り値として "クライアントとの接続が確立された新しいsocketインスタンス", "接続したクライアントのアドレス"が返ってくる
				print(f"=== Server: クライアントとの接続完了 remote_address: {address} ===")
				
				# クライアントを処理するスレッドを作成
				thread = Worker(client_socket, address)
				# スレッドを実行
				thread.start()
		finally:
			print("===サーバーを停止します===")

	def create_server_socket(self) -> socket:
		"""
		通信を待ち受けるためのserver_socketを生成する
		"""
		# socket生成
		server_socket = socket.socket()
		# socketのデフォルト設定ではプログラム終了後もしばらくportを掴んだまま離さないため設定変更
		server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		
		# bind: socketをlocalhostのポート8080に割り当てる/紐付ける（専有はしていない）
		server_socket.bind(("localhost", 8080))
		# listen: 接続要求の上限を10個としてbind済のポートを専有し接続を受け付けるようにする
		server_socket.listen(10)
		return server_socket