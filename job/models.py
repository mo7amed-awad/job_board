from django.db import models
import os
# Create your models here.

'''
django model field :
    -html widget
    -validation
    -db size
'''

JOB_TYPE=(
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

def image_upload(instance, filename):
    # Safely split the filename and extension
    imagename, extension = os.path.splitext(filename)
    return f"jobs/{instance.id}{extension}"

class Job(models.Model):
    title = models.CharField(max_length=100)
    job_title = models.CharField(max_length=15,choices=JOB_TYPE)#small amount
    description = models.TextField(max_length=1000)#large amount
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)

    # def save(self, *args, **kwargs):
    #     # Save the instance first to generate an ID if it doesn't exist
    #     if not self.id:
    #         super().save(*args, **kwargs)
    #     # Re-save to ensure the image uses the correct path
    #     return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name