from django.db import models
from django.shortcuts import render, redirect

class PhotoSet(models.Model):
    name = models.CharField(max_length=255)

class Photo(models.Model):
    photoset = models.ForeignKey(PhotoSet, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')

class Block1(models.Model):
    inscription = models.CharField(max_length=255)
    image = models.ImageField(upload_to='block1/')

class Block2(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

class Block2_Images(models.Model):
    image = models.ImageField(upload_to='block2/')

class Block5_contacts(models.Model):
    text = models.CharField(max_length=255)

class Block5_messages(models.Model):
    message_name = models.CharField(max_length=255)
    message_email = models.CharField(max_length=255)
    message_subject = models.CharField(max_length=255)
    message_text = models.TextField()
