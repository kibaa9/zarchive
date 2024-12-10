from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase
from zarchive.accounts.models import AppUser
from zarchive.authors.models import Author
from zarchive.books.models import Book
from zarchive.reviews.models import Review


class BookModelTest(TestCase):
    def setUp(self):
        self.user = AppUser.objects.create(username="testuser", password="password123")
        self.author = Author.objects.create(name="Author Name")

    def test_book_valid_creation(self):
        book = Book.objects.create(
            title="Test Book",
            author=self.author,
            description="Test Description",
            pages=200,
            year_of_publish=2000,
            publisher="Test Publisher",
            created_by=self.user,
        )
        self.assertEqual(book.title, "Test Book")
        self.assertEqual(book.author, self.author)
        self.assertEqual(book.pages, 200)
        self.assertEqual(book.year_of_publish, 2000)
        self.assertEqual(book.publisher, "Test Publisher")
        self.assertEqual(book.created_by, self.user)

    def test_book_title_unique_constraint(self):
        Book.objects.create(
            title="Unique Book",
            author=self.author,
            description="Description",
            pages=200,
            year_of_publish=2000,
            publisher="Publisher",
            created_by=self.user,
        )
        with self.assertRaises(IntegrityError):
            Book.objects.create(
                title="Unique Book",
                author=self.author,
                description="Description",
                pages=200,
                year_of_publish=2000,
                publisher="Publisher",
                created_by=self.user,
            )

    def test_book_year_of_publish_range(self):
        book = Book(
            title="Valid Year Book",
            author=self.author,
            description="Test Description",
            pages=200,
            year_of_publish=2000,
            publisher="Publisher",
            created_by=self.user,
        )
        book.full_clean()

        self.assertEqual(book.year_of_publish, 2000)

        book_low = Book(
            title="Low Year Book",
            author=self.author,
            description="Test Description",
            pages=200,
            year_of_publish=1799,
            publisher="Publisher",
            created_by=self.user,
        )
        with self.assertRaises(ValidationError):
            book_low.full_clean()

        book_low = Book(
            title="High Year Book",
            author=self.author,
            description="Test Description",
            pages=200,
            year_of_publish=2101,
            publisher="Publisher",
            created_by=self.user,
        )
        with self.assertRaises(ValidationError):
            book_low.full_clean()

    def test_book_pages_minimum_value(self):
        book1 = Book(
            title="Short Book",
            author=self.author,
            description="Test Description",
            pages=0,
            year_of_publish=2000,
            publisher="Publisher",
            created_by=self.user,
        )
        with self.assertRaises(ValidationError):
            book1.full_clean()

        book2 = Book(
            title="Too Short Book 2",
            author=self.author,
            description="Test Description",
            pages=-1,
            year_of_publish=2000,
            publisher="Publisher",
            created_by=self.user,
        )
        with self.assertRaises(ValidationError):
            book2.full_clean()

    def test_book_is_approved_default(self):
        book = Book.objects.create(
            title="Not Approved Book",
            author=self.author,
            description="Test Description",
            pages=200,
            year_of_publish=2000,
            publisher="Publisher",
            created_by=self.user,
        )
        self.assertFalse(book.is_approved)


class AuthorModelTest(TestCase):
    def test_valid_author_creation(self):
        author = Author.objects.create(
            name="Valid Author",
            bio="some author",
            date_of_birth="1980-04-04",
            date_of_death="1980-04-05",
        )
        self.assertEqual(author.name, "Valid Author")
        self.assertEqual(author.bio, "some author")
        self.assertEqual(author.date_of_birth, "1980-04-04")
        self.assertEqual(author.date_of_death, "1980-04-05")
        self.assertIsNone(author.profile_picture)

    def test_author_name_alpha_validator(self):
        author = Author(
            name="1 1",
            bio="Some author bio",
            date_of_birth="1980-04-04",
        )
        with self.assertRaises(ValidationError):
            author.full_clean()

        author2 = Author(
            name="Author Someone 2",
            bio="Some author bio",
            date_of_birth="1980-04-04",
        )
        with self.assertRaises(ValidationError):
            author2.full_clean()


class ReviewModelTests(TestCase):
    def setUp(self):
        self.user = AppUser.objects.create_user(username="testuser", password="password123")
        self.author = Author.objects.create(name="Author Name")
        self.book = Book.objects.create(
            title="Test Book",
            author=self.author,
            description="Description",
            pages=200,
            year_of_publish=2000,
            publisher="Test Publisher",
            created_by=self.user,
        )

    def test_unique_review_per_user_per_book(self):
        Review.objects.create(
            user=self.user,
            book=self.book,
            rating=4,
            comment="1",
        )
        duplicate_review = Review(
            user=self.user,
            book=self.book,
            rating=3,
            comment="2",
        )
        with self.assertRaises(ValidationError):
            duplicate_review.full_clean()

    def test_rating_validation(self):
        review = Review(
            user=self.user,
            book=self.book,
            rating=3,
            comment="Valid",
        )
        review.full_clean()

        invalid_review_low = Review(
            user=self.user,
            book=self.book,
            rating=0,
            comment="Invalid",
        )
        with self.assertRaises(ValidationError):
            invalid_review_low.full_clean()

        invalid_review_negative = Review(
            user=self.user,
            book=self.book,
            rating=-1,
            comment="Invalid",
        )
        with self.assertRaises(ValidationError):
            invalid_review_negative.full_clean()

        invalid_review_high = Review(
            user=self.user,
            book=self.book,
            rating=6,
            comment="Invalid",
        )
        with self.assertRaises(ValidationError):
            invalid_review_high.full_clean()
