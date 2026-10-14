class Book:
    pass


book_1 = Book()

book_1.title = "Python"
book_1.author = "omar shwaly"
book_1.price = 100


book_2 = Book()

book_2.title = "Data "
book_2.author = "saeed"
book_2.price = 200


print(
    f"First Book is title :{book_1.title} and author the Book {book_1.author} and price the Book = {book_1.price}"
)


print(
    f"second Book is title :{book_2.title} and author the Book {book_2.author} and price the Book = {book_2.price}"
)
