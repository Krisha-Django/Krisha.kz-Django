from django.db import models
from hotel.models import Hotel
from datetime import datetime


# Create your models here.
class CommentManager(models.Manager):
    def approved_comments(self):
        return super(CommentManager, self).get_queryset().filter(approved=True)

    def rejected_comments(self):
        return super(CommentManager, self).get_queryset().filter(approved=False)


class Comment(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='comments')
    # author = models.ForeignKey(User, on_delete = models.CASCADE, related _name= "comments")
    text = models.CharField(max_length=300)
    created_date = models.DateTimeField(default=datetime.now)
    approved = models.BooleanField(default=False)

    objects = CommentManager()

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
