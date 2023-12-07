class Book:
    def __init__(self, folder_path, file_name):
        self.folder_path = folder_path
        self.title = file_name
        self.text = self.read_text_from_file(folder_path, file_name)
        self.word_count = self.get_num_words()
        self.character_count = self.get_count_per_character()
        self.report = self.generate_report()
    
    def read_text_from_file(self, folder_path, file_name):
        path_to_file = folder_path + file_name

        with open(path_to_file) as f:
            return f.read()
        
    def get_num_words(self):
        return len(self.text.split())
    
    def get_count_per_character(self):
        unique_characters = {}
        text = self.text

        for c in text:
            if c.isalpha():
                if c not in unique_characters:
                    unique_characters[c] = 1
                else:
                    unique_characters[c] += 1

        return sorted(unique_characters.items())
    
    def generate_report(self):
        report = f"--- Begin report of {self.folder_path}{self.title} ---"
        report += "\n"
        report += f"{self.word_count} words found in the document"
        report += "\n"
        for k, v in self.character_count:
            report += "\n"
            report += f"The '{k}' character was found {v} times"
        report += "\n"
        report += "--- End report ---"

        return report
    
    def print_report(self):
        print(self.report)

    


    
