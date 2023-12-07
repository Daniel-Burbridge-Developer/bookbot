from book import Book
class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, folder_path, file_name):
        self.books.append(Book(folder_path, file_name))

    def report_book(self, book_title):
        for book in self.books:
            if book.title == book_title+".txt":
                book.print_report()

    def report_all_books(self):
        for book in self.books:
            book.print_report()


    