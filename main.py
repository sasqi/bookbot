from stats import number_of_words, count_chars, sort_chars

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def display_char_rows(dict):
    for i in dict:
        if i['char'].isalpha():
            print(f'{i['char']}: {i['num']}')

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    num_words = number_of_words(book_text)
    chars = sort_chars(count_chars(book_text))
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at ./books/frankenstein.txt ...')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print(f'--------- Character Count -------')
    display_char_rows(chars)
    print(f'============= END ===============')

main()