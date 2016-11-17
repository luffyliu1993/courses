from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

class Comment(models.Model):
    comment = models.TextField()
    course = models.ForeignKey('Course',on_delete=models.CASCADE, related_name='comment_course')
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
