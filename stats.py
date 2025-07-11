#returns number of words in the string
def get_num_words(text):
    words = len(text.split())
    return words

#returns the number of times each character is used
def get_num_char(text):
    num_char = {}
    for char in text:
        if char.lower() in num_char:
            num_char[char.lower()] +=1
        else:
            num_char[char.lower()] = 1
    return num_char


def sort_on(items):
    return items["num"]

def sort_dict(dict):
    new_list = []
    for char in dict:
        new_list.append({"char":char, "num":dict[char]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list