from rest_framework import serializers

from . import models


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ["*"]


class Genre(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = ["*"]


class Author(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = ["*"]
