import unittest

from app.Librairie import Book, Library, Client


class BookTestCase(unittest.TestCase):
    def setUp(self):
        self.book = Book("Title","Author")

    def test_check_out(self):
        self.book.check_out()
        self.assertTrue(self.book.is_checked_out)
    
    def test_check_in(self):
        self.book.check_out()
        self.book.check_in()
        self.assertFalse(self.book.is_checked_out)

class LibraryTestCase(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        book1 = Book("Title1","Author1")
        book2 = Book("Title2","Author2")
        book2.check_out()
        self.library.books.append(book1)
        self.library.books.append(book2)

    def test_add_book(self):
        book3 = Book("Title3","Author3")
        self.library.add_book(book3)
        with self.subTest():
            self.assertEqual(len(self.library.books),3)
        with self.subTest():
            self.assertEqual(self.library.books[-1].title,book3.title)

    def test_check_out_book(self):
        with self.subTest():
            self.library.check_out_book("Title1")
            self.assertTrue(self.library.books[0].is_checked_out)
        with self.subTest():
            self.library.check_out_book("Title2")
            self.assertTrue(self.library.books[1].is_checked_out)

    def test_check_in_book(self):
        with self.subTest():
            self.library.check_in_book("Title1")
            self.assertFalse(self.library.books[0].is_checked_out)
        with self.subTest():
            self.library.check_in_book("Title2")
            self.assertFalse(self.library.books[1].is_checked_out)

class ClientTestCase(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book("Title1","Author1")
        self.book2 = Book("Title2","Author2")
        self.book3 = Book("Title3","Author3")
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.add_book(self.book3)
        self.library.check_out_book("Title2")
        self.library.check_out_book("Title3")
        self.client = Client("NomClient")
        self.client.checked_out_books.append(self.book2)

    def test_check_out_book(self):
        self.client.check_out_book(self.library, "Title1")
        self.client.check_out_book(self.library, "Title2")
        self.client.check_out_book(self.library, "Title3")
        with self.subTest():
            self.assertTrue(self.library.books[0].is_checked_out)
        with self.subTest():
            self.assertTrue(self.library.books[1].is_checked_out)
        with self.subTest():
            self.assertTrue(self.library.books[2].is_checked_out)
        with self.subTest():
            self.assertTrue(self.book1 in self.client.checked_out_books)
        with self.subTest():
            self.assertTrue(self.book2 in self.client.checked_out_books)
        with self.subTest():
            self.assertFalse(self.book3 in self.client.checked_out_books)

    def test_check_in_book(self):
        self.client.check_in_book(self.library, "Title1")
        self.client.check_in_book(self.library, "Title2")
        self.client.check_in_book(self.library, "Title3")
        print(self.client.checked_out_books)
        with self.subTest():
            self.assertFalse(self.library.books[0].is_checked_out)
        with self.subTest():
            self.assertFalse(self.library.books[1].is_checked_out)
        with self.subTest():
            self.assertTrue(self.library.books[2].is_checked_out)
        with self.subTest():
            self.assertFalse(self.book1 in self.client.checked_out_books)
        with self.subTest():
            self.assertFalse(self.book2 in self.client.checked_out_books)
        with self.subTest():
            self.assertFalse(self.book3 in self.client.checked_out_books)