def count_words(text):
    words = text.split()
    return len(words)

def num_of_characters(text):
    number_of_characters = {}
    for char in text:
        lowercase_char = char.lower()
        if lowercase_char in number_of_characters:
            number_of_characters[lowercase_char] += 1
        else:
            number_of_characters[lowercase_char] = 1
    
    return number_of_characters


def sort_chars_by_count(char_dict):
    chars_list = []
    for char, count in char_dict.items():
        chars_list.append({"char": char, "num": count})
    
    def sort_on(dict):
        return dict["num"]
    
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list