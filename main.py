from library import Library
from os import listdir
def main():
    library = Library()

    for f in listdir("books"):
        library.add_book("books/", f)

    # library.report_all_books()
    library.report_book("frankenstein")
    # library.report_book("alice_in_wonderland")


if __name__ == "__main__":
    main()

