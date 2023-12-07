path_to_folder = "books/"
file_name = "frankenstein.txt"
path_to_file = path_to_folder + file_name

with open(path_to_file) as f:
    file_contents = f.read()
    
