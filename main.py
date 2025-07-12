from stats import get_num_words, get_num_char, sort_dict
import sys
if len(sys.argv) < 2:
    print("No path to file provided. Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    book_path = sys.argv[1]
    book_content = get_book_text(book_path)
    number_of_words = get_num_words(book_content)
    number_of_char = get_num_char(book_content)
    number_of_char = sort_dict(number_of_char)

    print(f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {number_of_words} total words
--------- Character Count -------""")
    for pair in number_of_char:
        if pair["char"].isalpha():
            print (f"{pair["char"]}: {pair["num"]}")


    print("============= END ===============")







main()
    