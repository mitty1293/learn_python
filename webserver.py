import os
import socket
from datetime import datetime
import traceback
from typing import Tuple
from urllib import response

class WebServer:
	"""
	Webサーバーを表すクラス
	"""

	# 実行ファイルのあるディレクトリ
	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	# 静的配信するファイルを置くディレクトリ
	STATIC_ROOT = os.path.join(BASE_DIR, "static")

	# 拡張子とMIME Typeの対応
	MIME_TYPES = {
		"html": "text/html",
		"css": "text/css",
		"png": "image/png",
		"jpg": "image/jpg",
		"gif": "image/gif"
	}

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
				print("===クライアントからの接続を待ちます===")
				(client_socket, address) = server_socket.accept()
				# 確立後、返り値として "クライアントとの接続が確立された新しいsocketインスタンス", "接続したクライアントのアドレス"が返ってくる
				print(f"===クライアントとの接続完了 remote_address: {address} ===")
				try:
					# クライアントと通信をしてリクエストを処理する
					self.handle_client(client_socket)
				except Exception:
						# リクエスト処理中に例外発生した際はコンソールにエラーを出力し処理続行
						print("=== リクエストの処理中にエラーが発生しました ===")
						traceback.print_exc()
				finally:
					# 例外の有無にかかわらずTCP通信のcloseは行う
					print("=== クライアントとの通信を終了します ===")
					client_socket.close()

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

	def handle_client(self, client_socket: socket) -> None:
		"""
		クライアントと接続済のsocketを引数とし、
		リクエストを処理してレスポンスを送信する
		"""
		# recv: クライアントから送られてきたデータをbytes型で4096バイトづつ取得する
		request = client_socket.recv(4096)
		
		# クライアントから送られてきたデータをファイルに書き出す
		with open("server_recv.txt", "wb") as f:
			f.write(request)
		
		# httpリクエストをパースする
		method, path, http_version, request_header, request_body = self.parse_http_request(request)

		try:
			# ファイルからレスポンスボディを生成
			response_body = self.get_static_file_content(path)
			# レスポンスラインを作成
			response_line = "HTTP/1.1 200 OK\r\n"
		except OSError:
			# ファイルが見つからなかった場合は404を返す
			response_body = b"<html><body><h1>404 Not Found</h1></body></html>"
			response_line = "HTTP/1.1 404 Not Found\r\n"
		
		# レスポンスヘッダーを生成
		response_header = self.build_response_header(path, response_body)

		# レスポンス全体を生成
		response = (response_line + response_header + "\r\n").encode() + response_body

		# クライアントへレスポンスを送信する
		client_socket.send(response)

	def parse_http_request(self, request: bytes) -> Tuple[str, str, str, bytes, bytes]:
		"""
		HTTPリクエストを
		1. method: str
		2. path: str
		3. http_version: str
		4. request_header: bytes
		5. request_body: bytes
		に分割/変換する
		"""

		# リクエスト全体を
		# 1. リクエストライン（1行目）
		# 2. リクエストヘッダー（2行目-空行）
		# 3. リクエストボディ（空行-）
		# にパースする
		request_line, remain = request.split(b"\r\n", maxsplit=1)
		request_header, request_body = remain.split(b"\r\n\r\n", maxsplit=1)

		# リクエストラインを文字列に変換してパース
		method, path, http_version = request_line.decode().split(" ")

		return method, path, http_version, request_header, request_body
	
	def get_static_file_content(self, path: str) -> bytes:
		"""
		リクエストpathからstaticファイルの内容を取得する
		"""
		# path先頭の/を削除し相対パスにする
		relative_path = path.lstrip("/")
		# ファイルのpathを取得
		static_file_path = os.path.join(self.STATIC_ROOT, relative_path)
		# ファイルからレスポンスボディを作成する
		with open(static_file_path, "rb") as f:
				return f.read()

	def build_response_header(self, path: str, response_body: bytes) -> str:
		"""
		レスポンスヘッダーを構築する
		"""
		# Content-Typeを取得する
		# pathから拡張子を取得
		if "." in path:
			ext = path.rsplit(".", maxsplit=1)[-1]
		else:
			ext = ""
		# 拡張子からMIME Typeを取得
		# 対応外の拡張子の場合はoctet-streamとする
		content_type = self.MIME_TYPES.get(ext, "application/octet-stream")

		# レスポンスヘッダーを作成する
		response_header = ""
		response_header += f"Date: {datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')}\r\n"
		response_header += "Host: pyServer/0.1\r\n"
		response_header += f"Content-Length: {len(response_body)}\r\n"
		response_header += "Connection: Close\r\n"
		response_header += f"Content-Type: {content_type}\r\n"
					
		return response_header

if __name__ == '__main__':
	server = WebServer()
	server.serve()
