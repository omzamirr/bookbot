from stats import count_words, num_of_characters, sort_chars_by_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    
    # Print report header
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    
    # Print word count
    print("----------- Word Count ----------")
    word_count = count_words(text)
    print(f"Found {word_count} total words")
    
    # Print character count
    print("--------- Character Count -------")
    char_counts = num_of_characters(text)
    sorted_chars = sort_chars_by_count(char_counts)
    
    # Print each alphabetical character and its count
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():  # Only print alphabetical characters
            print(f"{char}: {count}")
    
    # Print report footer
    print("============= END ===============")



if __name__ == "__main__":
    main()