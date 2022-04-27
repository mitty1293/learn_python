from typing import Callable, Optional

from henango.http.request import HTTPRequest
from henango.http.response import HTTPResponse
from henango.views.static import static
from urls import url_patterns

class URLResolver:
	def resolve(self, request: HTTPRequest) -> Callable[[HTTPRequest], HTTPResponse]:
		"""
		URL解決を行う
		# pathにマッチするurl_patternが存在すれば対応するviewを返す
		# 存在しなければstatic viewを返す
		"""
		for url_pattern in url_patterns:
			match = url_pattern.match(request.path)
			if match:
				request.params.update(match.groupdict())
				return url_pattern.view
		return static