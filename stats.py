def get_num_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_report(words, characters, file):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    sorted_chars = sorted(characters.items(), key=lambda characters: characters[1], reverse = True)
    for char in sorted_chars:
        if char[0].isalpha():
            print(f"{char[0]}: {char[1]}")
    print("============= END ===============")
