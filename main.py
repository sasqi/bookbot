import sys
from stats import get_num_words, get_chars_dict, chars_dict_to_sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def display_char_rows(dict):
    for i in dict:
        if i['char'].isalpha():
            print(f'{i['char']}: {i['num']}')

def main():
    if len(sys.argv) < 2:
        sys.exit('Usage: python3 main.py <path_to_book>')
    else:
        book_path = sys.argv[1]
        book_text = get_book_text(book_path)
        num_words = get_num_words(book_text)
        chars_dict = get_chars_dict(book_text)
        chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
        print('============ BOOKBOT ============')
        print(f'Analyzing book found at {book_path} ...')
        print('----------- Word Count ----------')
        print(f'Found {num_words} total words')
        print(f'--------- Character Count -------')
        display_char_rows(chars_sorted_list)
        print(f'============= END ===============')

main()