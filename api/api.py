from parse import parse
from webob import Request, Response


class API:
    def __init__(self):
        self.routes = {}

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.handel_request(request)
        return response(environ, start_response)

    def handel_request(self, request):
        response = Response()
        handler, args = self.find_handler(request_path=request.path)
        if handler is not None:
            handler(request, response, **args)
        else:
            self.defalut_response(response)
        return response

    def route(self, path):
        def wrapper(handler):
            self.routes[path] = handler
            return handler

        return wrapper

    def defalut_response(self, response):
        response.status_code = 404
        response.text = "Page not found"

    def find_handler(self, request_path):
        for path, handler, in self.routes.items():
            parse_result = parse(path, request_path)
            if parse_result is not None:
                return handler, parse_result.named
        return None, None
