from django.db import models


# Create your models here.
class Search(models.Model):
    location = models.CharField(max_length=500, default="")
    search = models.CharField(max_length=500, default="")
    result_index = models.CharField(max_length=500, default="")
    creation_date = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)

    def __str__(self):
        if self.search != "":
            string = '{}'.format(self.search)
        else:
            string = "~search-all"
        return string

    class Meta:
        verbose_name_plural = 'Searches'
        ordering = ['creation_date', ]
        get_latest_by = ['creation_date', ]


class Listing(models.Model):
    title = models.TextField(max_length=50, default="")
    url = models.TextField(max_length=500, default="")
    image_url = models.TextField(max_length=500, default="")
    hood = models.TextField(max_length=50, default="")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id', ]

