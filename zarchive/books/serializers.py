from rest_framework import serializers
from zarchive.authors.models import Author
from zarchive.books.models import Book
from zarchive.genres.models import Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']


class BookSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(), many=True)

    class Meta:
        model = Book
        fields = ['title',
                  'author',
                  'description',
                  'genre',
                  'pages',
                  'year_of_publish',
                  'publisher',
                  'created_at',
                  ]

    def validate(self, data):
        if not data['title']:
            raise serializers.ValidationError("Title is required.")
        if not data['author']:
            raise serializers.ValidationError("Author is required.")
        if data['pages'] <= 0:
            raise serializers.ValidationError("Pages must be greater than zero.")
        if not data['year_of_publish']:
            raise serializers.ValidationError("Year of publishing must be between 1800 and 2100")
        return data
