def count_words(book):
    return (len(book.split()))

def sort_key(dict):
    return dict["num"]

def count_characters(book):
    book = book.lower()
    charCount = {}
    for char in book:
        charCount[char] = 0
    for char in book:
        charCount[char] = charCount[char]+1
    return charCount

def sort_characters(charDic):
    charlist = []
    for char in charDic:
        if char.isalpha():
            charlist.append({"character": char, "num": charDic[char]})
    charlist.sort(reverse=True, key=sort_key)
    return charlist