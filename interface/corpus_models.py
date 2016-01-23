# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Comments(models.Model):
    archived = models.NullBooleanField()
    author = models.CharField(max_length=-1, blank=True, null=True)
    author_flair_css_class = models.CharField(max_length=-1, blank=True, null=True)
    author_flair_text = models.CharField(max_length=-1, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    controversiality = models.IntegerField(blank=True, null=True)
    created_utc = models.IntegerField(blank=True, null=True)
    distinguished = models.CharField(max_length=-1, blank=True, null=True)
    downs = models.IntegerField(blank=True, null=True)
    edited = models.CharField(max_length=-1, blank=True, null=True)
    gilded = models.IntegerField(blank=True, null=True)
    id = models.CharField(max_length=-1, blank=True, null=True)
    link_id = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    parent_id = models.CharField(max_length=-1, blank=True, null=True)
    retrieved_on = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    score_hidden = models.NullBooleanField()
    subreddit = models.CharField(max_length=-1, blank=True, null=True)
    subreddit_id = models.CharField(max_length=-1, blank=True, null=True)
    ups = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comments'


class CommentsAbridged(models.Model):
    archived = models.NullBooleanField()
    author = models.CharField(max_length=-1, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    controversiality = models.IntegerField(blank=True, null=True)
    created_utc = models.IntegerField(blank=True, null=True)
    downs = models.IntegerField(blank=True, null=True)
    gilded = models.IntegerField(blank=True, null=True)
    id = models.CharField(max_length=-1, blank=True, null=True)
    link_id = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    parent_id = models.CharField(max_length=-1, blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    score_hidden = models.NullBooleanField()
    subreddit = models.CharField(max_length=-1, blank=True, null=True)
    subreddit_id = models.CharField(max_length=-1, blank=True, null=True)
    ups = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comments_abridged'
