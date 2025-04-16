import sys
from stats import word_count
from stats import character_count
from stats import sort_char_dict

if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

path_to_file = sys.argv[1]

def get_book_text(filepath):

    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    
    num_words = word_count(path_to_file)
    character_count_dict = character_count(path_to_file)
    sorted_char_list = sort_char_dict(path_to_file)
    
    #Generating Report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char,count in sorted_char_list:
        print(f"{char}: {count}")
    print("============= END ===============")

main()