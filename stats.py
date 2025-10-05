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

    


