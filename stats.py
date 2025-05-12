def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text.lower():
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(dict):
    sorted_list = []
    for k,v in dict.items():
        sorted_list.append({'char': k, 'num': v})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list