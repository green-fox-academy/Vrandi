
class Mystring:
    def __init__(self, text):
        self.text = text

    def str_converter(self):
        stri = ''
        text = self.text.lower()
        for i in text:
            if text.count(i) == 1:
                stri += '('
            elif text.count(i) > 1:
                stri += ')'
        return stri


#"".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])
