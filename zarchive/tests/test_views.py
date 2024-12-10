from django.test import TestCase
from django.urls import reverse
from zarchive.accounts.models import AppUser
from zarchive.authors.models import Author
from zarchive.books.models import Book


class BookListViewTests(TestCase):
    def setUp(self):
        self.user = AppUser.objects.create_user(username="testuser", password="password123")
        self.author = Author.objects.create(name="Author Name")
        for i in range(15):
            Book.objects.create(
                title=f"Book {i + 1}",
                author=self.author,
                description="Description",
                pages=200,
                year_of_publish=2000,
                publisher="Publisher",
                created_by=self.user,
            )

    def test_book_list_view_pagination(self):
        response = self.client.get(reverse('book_catalogue_page'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['book_list']), 10)
        self.assertTemplateUsed(response, 'books/book_catalogue_page.html')


class BookDetailViewTests(TestCase):
    def setUp(self):
        self.user = AppUser.objects.create_user(username="testuser", password="password123")
        self.author = Author.objects.create(name="Author Name")
        self.book = Book.objects.create(
            title="Test Book",
            author=self.author,
            description="Description",
            pages=200,
            year_of_publish=2000,
            publisher="Publisher",
            created_by=self.user,
        )
        self.client.login(username="testuser", password="password123")

    def test_book_detail_view_context(self):
        response = self.client.get(reverse('book_detail_page', kwargs={'pk': self.book.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['book'], self.book)
        self.assertIn('reviews', response.context)
        self.assertTemplateUsed(response, 'books/book_detail_page.html')


class SearchBooksViewTests(TestCase):
    def setUp(self):
        self.user = AppUser.objects.create_user(username="testuser", password="password123")
        self.author = Author.objects.create(name="Author Name")
        self.book1 = Book.objects.create(
            title="Some Test Book",
            author=self.author,
            description="Description",
            pages=200,
            year_of_publish=2000,
            publisher="Publisher",
            created_by=self.user,
        )
        self.book2 = Book.objects.create(
            title="Some Test Book 2",
            author=self.author,
            description="Description 2",
            pages=201,
            year_of_publish=2001,
            publisher="Publisher 2",
            created_by=self.user,
        )

    def test_search_books_view(self):
        response = self.client.get(reverse('book_search_page'), {'q': 'Some'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.book1, response.context['books'])
        self.assertIn(self.book2, response.context['books'])
        self.assertTemplateUsed(response, 'books/book_search_page.html')
