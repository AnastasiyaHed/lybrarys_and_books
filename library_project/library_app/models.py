from django.db import models

class MediaResource(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        abstract = True

class Book(MediaResource):
    author = models.CharField(max_length=255)
    library = models.ForeignKey('Library', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Author(MediaResource):
    name = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, blank=True)


class Library(MediaResource):
    location = models.CharField(max_length=255, blank=True)
    established_date = models.DateField(null=True, blank=True)