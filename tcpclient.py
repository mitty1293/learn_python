import socket, codecs

class TCPClient:
	"""
	TCP通信を行うクライアントを表すクラス
	"""
	def request(self):
		"""
		サーバーへリクエストを送信するメソッド
		"""
		print("===クライアントを起動します===")
		
		try:
			# socketを生成
			client_socket = socket.socket()
			# socketのデフォルト設定ではプログラム終了後もしばらくportを掴んだまま離さないため設定変更
			client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			
			# connect: サーバー（localhostのポート80）へ接続する
			print("===サーバーと接続します===")
			client_socket.connect(("localhost", 80))
			print("===サーバーとの接続が完了しました===")
			
			# サーバーに送信するリクエストをファイルから取得する
			with open("client_send.txt", "rb") as f:
				request = f.read()
			
			# send: 接続済socketインスタンスに対しsendを呼び出し、サーバーへリクエストを送信する
			# 引数requestはbytes型でないといけないことに注意
			client_socket.send(request)
			
			# サーバーからレスポンスが送られてくるのを待ち取得する
			# recv: サーバから送られてきたレスポンスデータをbytes型で4096バイトづつ取得する
			response = client_socket.recv(4096)
			
			# レスポンス内容をファイルに書き出す
			with open("client_recv.txt", "wb") as f:
				f.write(response)
			
			# 通信を終了させる
			client_socket.close()
		
		finally:
			print("===クライアントを停止します===")

if __name__ == '__main__':
	client = TCPClient()
	client.request()
