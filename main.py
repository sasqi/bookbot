from stats import number_of_words, count_chars

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()



def main():
    book_text = get_book_text("./books/frankenstein.txt")
    num_words = number_of_words(book_text)
    print(f'{num_words} words found in the document')
    print(count_chars(book_text))


main()