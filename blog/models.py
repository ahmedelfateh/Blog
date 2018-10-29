from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    # Fields
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    # Methods

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    # Fields
    post = models.ForeignKey(
        'blog.Post', on_delete=models.DO_NOTHING, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_commnets = models.BooleanField(default=True)

    # Methods

    def approve(self):
        self.approved_commnets = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        self.text
