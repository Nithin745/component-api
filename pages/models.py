from django.db import models

# Create your models here.


class Type(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Content(models.Model):
    main_content = models.TextField(max_length=500, null=True)
    sub_content = models.TextField(max_length=500, null=True)
    image = models.ImageField(upload_to='images/', null=True)
    type = models.ForeignKey(
        Type, on_delete=models.CASCADE, related_name='content_type')

