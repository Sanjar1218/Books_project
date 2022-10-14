from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

class Books(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')
    total_pages = models.DecimalField(decimal_places=0, max_digits=4)
    published_date = models.DateField(auto_now_add=True)
    genres = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title