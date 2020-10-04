from django.db import models
# How exactly do Django content types work?
# https://stackoverflow.com/questions/20895429/how-exactly-do-django-content-types-work
# https://simpleisbetterthancomplex.com/tutorial/2016/10/13/how-to-use-generic-relations.html
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

import users.models

# Create your models here.
class Problem(models.Model):
    title = models.CharField(max_length=10000)
    description = models.CharField(max_length=10000)
    company = models.ForeignKey(
        users.models.Company,
        on_delete=models.CASCADE,
    )
    date_posted = models.DateTimeField()
    # course_content contains all the course content of a problem
    # the JSON is a list of basic elements that includes type and data
    # sample content: {[
    #     {"type": "text", "content": "Here is a piece of text"},
    #     {"type": "video", "url": "https://example.com/link_to_video"},
    #     {"type": "text", "content": "Here is another piece of text"},
    #     {"type": "image", "url": "https://example.com/link_to_image"}
    # ]}
    # course_content = models.JSONField()
    def __str__(self):
        return self.title

class Solution(models.Model):
    date_solved = models.DateTimeField()
    problem = models.ForeignKey('Problem', on_delete=models.CASCADE)
    professor = models.ForeignKey(
        users.models.Professor,
        on_delete=models.CASCADE,
    )
    video_url = models.URLField(null=True)
    solution_text = models.TextField()

    def __str__(self):
        return self.problem.title + '/' + self.professor.full_name

class Discussion(models.Model):
    problem = models.ForeignKey('Problem', on_delete=models.CASCADE)
    student = models.ForeignKey(users.models.Student, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.problem.title + '/' + self.student.full_name + '/' + self.comment
