from parse import parse

from api.request_handler import RequestHandler
from api.respone_handler import ResponseHandler


class API:
    def __init__(self):
        self.routes = {}

    def __call__(self, environ, start_response):
        request_handler = RequestHandler(environ)
        response = self.handel_request(request_handler)
        return response(environ, start_response)

    def handel_request(self, request):
        response = ResponseHandler()
        handler, args = self.find_handler(request_path=request.path)
        if handler is not None:
            handler(request, response, *args)
        else:
            self.defalut_response(response)
        return response

    def route(self, path):
        def wrapper(handler):
            self.routes[path] = handler
            return handler

        return wrapper

    def defalut_response(self, response: ResponseHandler):
        response.status_code = 404
        response.set_body = "Page can't load"

    def find_handler(self, request_path):
        for path, handler, in self.routes.items():
            parse_result = parse(path, request_path)
            if parse_result is not None:
                return handler, parse_result.named
        return None, None
