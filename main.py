def main():

    path_to_folder = "books/"
    file_name = "frankenstein.txt"
    book = set_book(path_to_folder, file_name)
    print(get_num_words(book))

def set_book(path_to_folder, file_name):
    path_to_file = path_to_folder + file_name

    with open(path_to_file) as f:
        return f.read()
    
def get_num_words(book):
    return len(book.split())

if __name__ == "__main__":
    main()

