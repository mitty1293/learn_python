import urllib.parse
from datetime import datetime
from pprint import pformat

from henango.http.request import HTTPRequest
from henango.http.response import HTTPResponse
from henango.template.renderer import render

def now(request: HTTPRequest) -> HTTPResponse:
    """
    pathが/nowのときは現在時刻を表示するHTMLを生成
    """
    context = {"now": datetime.now()}
    body = render("now.html", context)
    
    return HTTPResponse(body=body)

def show_request(request: HTTPRequest) -> HTTPResponse:
    """
    pathが/show_requestのときはHTTPリクエスト内容を表示するHTMLを生成
    """
    context = {"request": request, "headers": pformat(request.headers), "body": request.body.decode("utf-8", "ignore")}
    body = render("show_request.html", context)
    
    return HTTPResponse(body=body)

def parameters(request: HTTPRequest) -> HTTPResponse:
    """
    pathが/parametersのときはPOSTパラメータを表示するHTMLを生成する
    """
    # GETメソッドの時は405を返す
    if request.method == "GET":
        body = b"<html><body><h1>405 Method Not Allowed</h1></body></html>"

        return HTTPResponse(body=body, status_code=405)

    elif request.method == "POST":
        context = {"params": urllib.parse.parse_qs(request.body.decode())}
        body = render("parameters.html", context)

        return HTTPResponse(body=body)

def user_profile(request: HTTPRequest) -> HTTPResponse:
    context = {"user_id": request.params["user_id"]}
    body = render("user_profile.html", context)
        
    return HTTPResponse(body=body)

def set_cookie(request: HTTPRequest) -> HTTPResponse:
    return HTTPResponse(headers={"Set-Cookie": "username=TARO"})