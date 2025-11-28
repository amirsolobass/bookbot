from stats import count_words, count_chars, sort_list

def get_book_text(file_path):
    with open(file_path) as file: # Open the book file
        book_text = file.read() # Read the entire content
        return book_text


def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path) # Get book text
    count = count_words(book_text) # Count words
    char_counts = count_chars(book_text) # Count characters
    char_counts = sort_list(char_counts) # Sort character counts
    print("============ BOOKBOT ============")
    print(f"Analyzing book at: {book_path}")
    print("=================================")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for char, count in char_counts: # Print each character and its count as a list
        print(f"{char}: {count}")
    print("============= END ===============")
    
main()