from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

class Books(models.Model):
    title = models.CharField(max_length=50)
    total_pages = models.DecimalField()
    published_date = models.DateField(auto_now_add=True)
    genres = models.CharField(max_lenght=30)
    author = models.ForeignKey(Author)

    def __str__(self):
        return self.title