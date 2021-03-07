from django.db import models


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    cat = models.ForeignKey('Cat', related_name='posts', on_delete=models.PROTECT, null=True)

    class Meta:
        ordering = ['created']


class Cat(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    root = models.BooleanField()
    parent_id = models.IntegerField(null=True, default=1)


