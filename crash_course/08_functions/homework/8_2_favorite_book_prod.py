# 8.2 favorite book production version
## Task ## : 8.2

def favorite_book(book: str | None = None) -> str:
    """
    I show how write like middle,senior Python programmer
    the same task solution 8.2
    """
    if not book:
        book = 'Alice in Wonderland'
    return f"One of my favorite books is {book}"

def book_message(book: str) -> None:
    """
    Print the favorite book!
    """
    print(favorite_book(book))

if __name__ == "__main__":
    book_message('Learn Python')
