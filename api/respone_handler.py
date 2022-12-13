class ResponseHandler:

    def __init__(self):
        self.status_code: int = 0
        self.headers: list[str] = []
        self.body: str = ""

    def set_header(self, header: str):
        self.headers.append(header)

    def set_headers(self, header: list[str]):
        self.headers.extend(header)

    def set_status_code(self, status_code: int):
        self.status_code = status_code

    def set_body(self, body: str, encoding: str = 'UTF-8'):
        self.body = body.encode(encoding=encoding)

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
