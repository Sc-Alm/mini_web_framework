import json


class ResponseHandler:

    def __init__(self):
        self.status_code: str = ""
        self.headers: list[str] = []
        self.body: str = ""
        self.json_body: dict[str: object] = None

    def set_header(self, header: str):
        self.headers.append(header)

    def set_headers(self, header: list[str]):
        self.headers.extend(header)

    def set_status_code(self, status_code: str):
        self.status_code = status_code

    def set_body(self, body: str, encoding: str = 'UTF-8'):
        self.body = body.encode(encoding=encoding)

    def set_json_body(self, json_body: dict[str: object], encoding: str = 'UTF-8'):
        self.json_body = json.dumps(json_body, separators=(',', ':'), default=str).encode(encoding=encoding)
        print(self.json_body)

    def _get_header_dict(self) -> dict[str, str]:
        result = {}
        if self.headers is not None:
            for header in self.headers:
                key, value = header.split(':')
                result[key] = value
        return result

    def _set_content_length(self):
        if self._get_header_dict().get('Content-Length') is None:
            self.set_header(f'Content-Length: {len(self.body)}')

    def _get_header_list(self):
        header_list = [
            ("Content-Type", self._get_header_dict()['Content-Type']),
            ("Content-Length", str(self._set_content_length()))
        ]
        return header_list

    def __call__(self, environ, start_response):
        if self.headers is not None:
            self.set_status_code("200 OK")
            start_response(self.status_code, self._get_header_list())
            if self._get_header_dict()['Content-Type'] == "application/json":
                return [self.json_body]
            else:
                return [self.body]

        else:
            self.set_status_code("404")
            start_response(self.status_code, self._get_header_list())
