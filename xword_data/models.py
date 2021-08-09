from django.db import models

# Create your models here.

class Puzzle(models.Model):
    title = models.CharField(blank=True, max_length=255)
    date = models.DateField('date published')
    byline = models.CharField(blank=False, max_length=255)
    publisher = models.CharField(blank=False, max_length=12)

class Entry(models.Model):
    entry_text = models.CharField(blank=False, unique=True, max_length=50)

class Clue(models.Model):
    entry = models.ForeignKey(
        Entry,
        on_delete = models.CASCADE,
    )
    puzzle = models.ForeignKey(
        Puzzle,
        on_delete = models.CASCADE
    )
    clue_text = models.CharField(blank=False, max_length=512)
    theme = models.BooleanField(default=False)

    def __str__(self):
        return self.clue_text

        