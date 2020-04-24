from django.core.exceptions import ValidationError
from django.db import models
from hotel.models import Hotel
from auth_.models import MyUser
from datetime import datetime
from .validators import validated_created_date, validated_text


# Create your models here.
class CommentManager(models.Manager):
    def approved_comments(self):
        return super(CommentManager, self).get_queryset().filter(approved=True)

    def rejected_comments(self):
        return super(CommentManager, self).get_queryset().filter(approved=False)


class Comment(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    text = models.CharField(max_length=300, validators=[validated_text])
    created_date = models.DateTimeField(auto_now_add=True, blank=True, validators=[validated_created_date])
    approved = models.BooleanField(default=False)

    objects = CommentManager()

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
