from stats import get_num_words, count_characters, sort_characters, sort_on
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]    
p = count_characters(path)
r = sort_characters(p)
print(f"============ BOOKBOT ============\n Analyzing book found at books/frankenstein.txt...\n ----------- Word Count ----------")
get_num_words(path)
print("-------- Character Count --------")
for item in r:
    print(f"{item['char']}: {item['num']}")
print("============= END ===============")


