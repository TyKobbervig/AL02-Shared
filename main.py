from catalog_data import BOOKS, validate_book_ids


def scan_lookup(records, book_id):
    """Return the first matching book or None."""
    for book in records:
        if book["id"] == book_id:
            return book
    return None


def build_index(records):
    """Build a dictionary mapping IDs to book records."""
    index = {}

    for book in records:
        index[book["id"]] = book

    return index


def indexed_lookup(index, book_id):
    """Return the matching book or None."""
    return index.get(book_id)


def display_book(book):
    """Display book information."""
    if book is None:
        print("Book not found.")
    else:
        print(
            f"ID: {book['id']}, "
            f"Title: {book['title']}, "
            f"Author: {book['author']}"
        )


def main():
    # Validate IDs before comparing lookup approaches
    validate_book_ids(BOOKS)

    # Build dictionary index
    index = build_index(BOOKS)

    # Test B1
    print("Scan Lookup for B1:")
    display_book(scan_lookup(BOOKS, "B1"))

    # Test B4
    print("\nIndexed Lookup for B4:")
    display_book(indexed_lookup(index, "B4"))

    # Test absent ID
    print("\nLookup for B99:")
    display_book(scan_lookup(BOOKS, "B99"))
    
    # Empty Input
    print("\nScan Lookup with empty input:")
    display_book(scan_lookup([], "B1"))

    print("\nIndexed Lookup with empty input:")
    display_book(indexed_lookup({}, "B1"))


if __name__ == "__main__":
    main()
    
