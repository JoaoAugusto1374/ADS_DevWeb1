from datetime import datetime 
from urllib import parse 
from .constants import status_codes

class Request:
    def __init__(self, request_bytes, addr):
        request = request_bytes.decode("utf-8")

        header, body = request.split("\r\n\r\n", 1)
        request_line, *header_lines = header.split("\r\n")

        method, uri, http_version = request_line.split(" ")

        parsed_uri = parse.urlparse(uri)

        self.datetime = datetime.now()
        self.ip = addr[0]
        self.method = method
        self.uri = uri 
        self.path = parsed_uri.path
        self.queries = parse.parse_qs(parsed_uri.query)
        self.http_version = http_version 
        self.headers = self.parse_headers(header_lines)
        self.body = body 

    def parse_headers(self, header_lines):
        headers = {}
        for line in header_lines:
            key, value = line.split(":", 1)
            headers[key.lower()] = value.strip()
        return headers 


class Response:
    def __init__(self, headers=None, body="", status_code=200, status_message=None):
        self.headers = headers or {}
        self.body = body 
        self._status_message_changed = (status_message is not None)
        self.status_message = status_message or None
        self.status_code = status_code 

    @property
    def status_message(self):
        if not self._status_message_changed:
            return status_codes.get(self.status_code, "???")
        return self._status_message

    @status_message.setter
    def status_message(self, message):
        self._status_message = message
        self._status_message_changed = True

    def serialize(self):
        status_line = f"HTTP/1.1 {self.status_code} {self.status_message}"
        headers = "\r\n".join([f"{key}: {value}" for key, value in self.headers.items()])
        header_section = "\r\n".join([status_line, headers])
        http_response = "\r\n\r\n".join([header_section, self.body])
        return http_response.encode("utf-8")
