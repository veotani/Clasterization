class Document:
    body = ''
    category = ''

    def __init__(self, _category, _title, _body):
        self.category = _category
        self.body = _title + ' ' + _body
