def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(items):
    return items["num"]

def convert_dict(char_dict):
    char_dict_list = []
    for k in char_dict:
        char_dict_list.append({"char": k,"num": char_dict[k]})
    char_dict_list.sort(reverse=True, key=sort_on)
    return char_dict_list