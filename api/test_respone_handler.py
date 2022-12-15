from unittest import TestCase

from .respone_handler import ResponseHandler

TEST_HEADERS = [
    "Content-Type: text/html",
    "Content-Length: 200"
]


class TestResponseHandler(TestCase):
    def setUp(self) -> None:
        self.response_handler = ResponseHandler()
        self.response_handler.set_headers(TEST_HEADERS)

    def test__get_header_dict(self):
        print(self.response_handler._get_header_list())
