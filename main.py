import sys
from stats import get_num_words, get_chars_dict, convert_dict, sort_on

if len(sys.argv) < 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    print(file_contents)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(path, count, dict_list):
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {path}...')
    print('----------- Word Count ----------')
    print(f'Found {count} total words')
    print('--------- Character Count -------')
    for k in dict_list:
        if k['char'].isalpha():
            print(f'{k['char']}: {k['num']}')
    print('============= END ===============')

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    # print(f"{num_words} words found in the document")
    # print(chars_dict)
    char_dict_list = convert_dict(chars_dict)
    # print(char_dict_list)
    print_report(book_path, num_words, char_dict_list)

main()