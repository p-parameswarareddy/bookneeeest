from django.test import TestCase

class BookModelTest(TestCase):
    def test_create_book(self):
        book = Book.objects.create(
            title="Test Book",
            author="Author",
            published_date="2023-01-01",
            isbn="1234567890123"
        )
        self.assertEqual(str(book), "Test Book")

