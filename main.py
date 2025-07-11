from stats import get_num_words, get_num_char
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    book_content = get_book_text("books/frankenstein.txt")
    number_of_words = get_num_words(book_content)
    number_of_char = get_num_char(book_content)
    print(f"{number_of_words} words found in the document")
    print(f"{number_of_char}")





main()
    