from django.db import models

# Create your models here.
# class Tag(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=200)
#     event = models.ManyToManyField('Event', related_name='tags')
#     def __str__(self):
#         return self.name

# class Event(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=200)
#     start_time = models.DateTimeField()
#     duration = models.IntegerField()
#     location = models.CharField(max_length=200)
#     image_url = models.CharField(max_length=200)
#     registration_link = models.CharField(max_length=200)
#     short_description = models.TextField()
#     long_description = models.TextField()
#     def __str__(self):
#         return self.name