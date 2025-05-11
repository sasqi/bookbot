def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def number_of_words(text):
    words = text.split()
    return len(words)


def main():
    num_words = number_of_words(get_book_text("./books/frankenstein.txt"))
    print(f'{num_words} words found in the document')


main()