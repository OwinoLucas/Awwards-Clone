from django.db import models

# Create your models here.
class Projects(models.Model):
    """
    class containing projects' objects
    """
    project_name = models.CharField(max_length=50, blank=True)
    project_image = models.ImageField(upload_to='projectimages/', blank=True)
    description = models.TextField(max_length=300, blank=True)
    github_repo = models.CharField(max_length=150, blank=True)
    url = models.CharField(max_length=50, blank=True)