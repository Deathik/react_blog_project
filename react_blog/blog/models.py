from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=100)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pub_date']

    def edited(self):
        if self.pub_date < self.last_modified:
            if (self.last_modified - self.pub_date).seconds <= 0:
                return False
        return True


    def get_absolute_url(self):
        return reverse('blog:post_edit', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
