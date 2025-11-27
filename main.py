def get_book_text(file_path):
    with open(file_path) as file:
        book_text = file.read()
        return book_text

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    print(book_text)

main()