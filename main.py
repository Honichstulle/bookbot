import sys
from stats import count_words
from stats import count_characters
from stats import sort_dictionaries

def get_book_text(path):
    with open(path) as b:
        return b.read()
    
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_characters = count_characters(text)
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {book_path}...")
    print ("----------- Word Count ----------")
    print (f"Found {num_words} total words")
    print ("----------- Character Count ----------")
    for c in sort_dictionaries(num_characters):
        if c["char"].isalpha() == False:
            continue
        else:
            char = c["char"]
            num = c["num"]
            print(f"{char}: {num}")
    print("============= END ===============")


main()

    
