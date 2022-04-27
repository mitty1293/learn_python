import os
import traceback

import settings
from henango.http.request import HTTPRequest
from henango.http.response import HTTPResponse

def static(request: HTTPRequest) -> HTTPResponse:
	"""
	静的ファイルからレスポンスを生成する
	"""
	try:
		static_root = getattr(settings, "STATIC_ROOT")
		# path先頭の/を削除し相対パスにする
		relative_path = request.path.lstrip("/")
		# ファイルのpathを取得
		static_file_path = os.path.join(static_root, relative_path)
		# ファイルからレスポンスボディを作成する
		with open(static_file_path, "rb") as f:
			response_body = f.read()
		content_type = None
		return HTTPResponse(body=response_body, content_type=content_type, status_code=200)
	
	except OSError:
		# レスポンスを取得できない（ファイルが見つからなかった等）場合はログ出力して404を返す
		traceback.print_exc()
		response_body = b"<html><body><h1>404 Not Found</h1></body></html>"
		content_type = "text/html;"
		return HTTPResponse(body=response_body, content_type=content_type, status_code=404)
			