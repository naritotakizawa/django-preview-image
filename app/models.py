from django.db import models


class Image(models.Model):
    file = models.ImageField('画像ファイル')

    def __str__(self):
        return self.file.name
