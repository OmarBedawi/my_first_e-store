from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Ebook(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)  # noqa: disable=line-too-long
    sku = models.CharField(max_length=254, blank=True)
    title = models.CharField(max_length=254)
    authors = models.CharField(max_length=254, default='')
    year = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=1, null=True, blank=True)  # noqa: disable=line-too-long
    image_url = models.URLField(max_length=1024, blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title


class Ebook_reader(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)  # noqa: disable=line-too-long
    sku = models.CharField(max_length=254, blank=True)
    brand = models.CharField(max_length=254)
    model = models.CharField(max_length=254, default='')
    size = models.CharField(max_length=254, default='')
    memory = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=1, null=True, blank=True)  # noqa: disable=line-too-long
    image_url = models.URLField(max_length=1024, blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.model
