from .Book import Book

def main():
    library = Library()
    library.add_book("books/frankenstein.txt")
    library.report_all_books()

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, folder_path, file_name):
        self.books.append(Book(folder_path, file_name))

    def report_book(self, book):
        if book in self.books:
            book.print_report()

    def report_all_books(self):
        for book in self.books:
            book.print_report()