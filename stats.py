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

def sort_on(dict):
    return dict["num"]

def sort_chars(chars):
    output = []
    for k,v in chars.items():
        output.append({'char': k, 'num': v})
    output.sort(reverse=True, key=sort_on)
    return output