import logging
import requests


class DingDingHandler(logging.Handler):
    def __init__(self, webhook, toaddrs, timeout=10):
        logging.Handler.__init__(self)
        self.webhook = webhook
        self.toaddrs = toaddrs
        self.timeout = timeout

    def emit(self, record):
        post_data = {
            "msgtype": "text",
            "text": {
                "content": self.format(record)
            },
            "at": {
                "atMobiles": self.toaddrs,
                "isAtAll": False
            }
        }
        try:
            requests.post(self.webhook, json=post_data, timeout=self.timeout)
        except Exception:
            self.handleError(record)
