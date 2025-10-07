# Counts the words in a text

def count_words(text):
    return len(text.split())

# Counts single characters in a text

def count_characters(text):
    charcters = {}
    for c in text.lower():
        if c in charcters:
            charcters[c] += 1
        else:
            charcters[c] = 1
    return charcters


# Return num Value of a Dictionary
def sort_on(items):
    return items["num"]

# Creates a sorted list of dictionaries

def sort_dictionaries(d):
    li = []
    for key, value in d.items():
        new_dict = {"char": key, "num": value}
        li.append(new_dict)
        li.sort(reverse=True, key=sort_on)


    return li