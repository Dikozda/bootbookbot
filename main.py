from stats import count_words
from stats import count_characters
from stats import sort_characters
import sys

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    bookText = get_book_text(filepath)
    characters = count_characters(bookText)
    sortedCarh = sort_characters(characters)
    print (f"============ BOOKBOT ============\nAnalyzing book found at {filepath}...\n----------- Word Count ----------\nFound {count_words(bookText)} total words\n--------- Character Count -------")
    for char in sortedCarh:
        print (f"{char["character"]}: {char["num"]}\n")
    print ("============= END ===============")

main()