def number_of_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    chars = {}
    for c in text.lower():
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars