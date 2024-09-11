class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_summary(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"
