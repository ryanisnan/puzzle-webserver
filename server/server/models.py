from django.db import models
from s3direct.fields import S3DirectField


class Puzzle(models.Model):
    name = models.CharField(max_length=256, default='')
    released_at = models.DateTimeField(help_text='When do you want this puzzle to release at?')
    puzzle = S3DirectField(dest='puzzles', unique=True)

    def __unicode__(self):
        return self.name
