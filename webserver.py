import socket
from datetime import datetime

class WebServer:
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
			server_socket = socket.socket()
			# socketのデフォルト設定ではプログラム終了後もしばらくportを掴んだまま離さないため設定変更
			server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			
			# bind: socketをlocalhostのポート8080に割り当てる/紐付ける（専有はしていない）
			server_socket.bind(("localhost", 8080))
			# listen: 接続要求の上限を10個としてbind済のポートを専有し接続を受け付けるようにする
			server_socket.listen(10)
			
			# accept: 接続を待ち、接続があればコネクションを確立する
			print("===クライアントからの接続を待ちます===")
			(client_socket, address) = server_socket.accept()
			# 確立後、返り値として "クライアントとの接続が確立された新しいsocketインスタンス", "接続したクライアントのアドレス"が返ってくる
			print(f"===クライアントとの接続完了 remote_address: {address} ===")
			
			# recv: クライアントから送られてきたデータをbytes型で4096バイトづつ取得する
			request = client_socket.recv(4096)
			
			# クライアントから送られてきたデータをファイルに書き出す
			with open("server_recv.txt", "wb") as f:
				f.write(request)
			
			# レスポンスボディを作成する
			response_body = "<html><body><h1>It works!</h1></body></html>"
			# レスポンスラインを作成する
			response_line = "HTTP/1.1 200 OK\r\n"
			# レスポンスヘッダーを作成する
			response_header = ""
			response_header += f"Date: {datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')}\r\n"
			response_header += "Host: pyServer/0.1\r\n"
			response_header += f"Content-Length: {len(response_body.encode())}\r\n"
			response_header += "Connection: Close\r\n"
			response_header += "Content-Type: text/html\r\n"
			
			# ヘッダーとボディを空行で結合しbytesに変換、レスポンス全体を生成する
			response = (response_line + response_header + "\r\n" + response_body).encode()
			
			# クライアントへレスポンスを送信する
			client_socket.send(response)
			
			# 返事は返さずに通信を終了させる
			client_socket.close()
		
		finally:
			print("===サーバーを停止します===")

if __name__ == '__main__':
	server = WebServer()
	server.serve()
