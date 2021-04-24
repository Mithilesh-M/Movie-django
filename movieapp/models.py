from django.db import models
import uuid

class Movie(models.Model):
    title = models.CharField(max_length=200)
    prefix = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    director = models.ManyToManyField('Director')
    studio = models.ForeignKey('Studio',on_delete=models.CASCADE)
    released_date = models.DateField()
    cover_image = models.ImageField(upload_to='movieapp/static/images',null=True,blank=True)
    review = models.TextField(max_length=500)
    genre = models.ManyToManyField('Genre')
    asin = models.UUIDField(unique=True, default=uuid.uuid4)

    def __str__(self):
        """String for representing the Model object."""
        return self.title

class Studio(models.Model):
    title = models.CharField(max_length=200)
    prefix = models.CharField(max_length=200)
    website = models.URLField(null=True, blank=True)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        """String for representing the Model object."""
        return self.title

class Genre(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        """String for representing the Model object."""
        return self.title

class Director(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    website = models.URLField(null=True, blank=True)
    birthday = models.DateField()
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER,
        blank=True,
        help_text='gender',
    )
    def __str__(self):
        """String for representing the Model object."""
        return self.first_name
