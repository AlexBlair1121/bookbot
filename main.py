from stats import get_num_words, character_count, get_report
import sys

def main(): 
    if len(sys.argv) < 2:
        print("Please input commands like so, Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
        text = get_book_text(filepath)
        num_words = get_num_words(text)
        #print(f"{num_words} words found in the document")
        characters = character_count(text)
        #print(characters)
        #print(text)
        report = get_report(num_words, characters, filepath)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

# def print_report(book_path, num_words, chars_sorted_list):
#     print("============ BOOKBOT ============")
#     print(f"Analyzing book found at {book_path}...")
#     print("----------- Word Count ----------")
#     print(f"Found {num_words} total words")
#     print("--------- Character Count -------")
#     for item in chars_sorted_list:
#         if not item["char"].isalpha():
#             continue
#         print(f"{item['char']}: {item['num']}")

#     print("============= END ===============")

main()
