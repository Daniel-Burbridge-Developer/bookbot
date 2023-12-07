def main():

    path_to_folder = "books/"
    file_name = "frankenstein.txt"
    book = set_book(path_to_folder, file_name)
    print(generate_report(calc_num_words(book), calc_count_per_character(book)))

def set_book(path_to_folder, file_name):
    path_to_file = path_to_folder + file_name

    with open(path_to_file) as f:
        return f.read()
    
def calc_num_words(text):
    return len(text.split())

def calc_count_per_character(text):
    unique_characters = {}
    text = text.lower()

    for c in text:
        if c.isalpha():
            if c not in unique_characters:
                unique_characters[c] = 1
            else:
                unique_characters[c] += 1

    return sorted(unique_characters.items())

def generate_report(word_count, character_count_dict):
    report = "--- Begin report of books/frankenstein.txt ---"
    report += "\n"
    report += f"{word_count} words found in the document"
    report += "\n"
    for k, v in character_count_dict:
        report += "\n"
        report += f"The '{k}' character was found {v} times"
    report += "\n"
    report += "--- End report ---"

    return report


if __name__ == "__main__":
    main()

