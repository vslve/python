from django.db import models


class Image(models.Model):
    name = models.CharField(max_length=25, default='image')
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    size = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'


class Comment(models.Model):
    text = models.TextField(max_length=250)
    image = models.ForeignKey(Image, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text[:15]}'
