class NotDictKeyError(Exception):
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message


class HeadItemNotFound(Exception):
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message
