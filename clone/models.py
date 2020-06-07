from django.db import models
from django.contrib.auth.models import User


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

    def __str__(self):
        return self.url

class Profile(models.Model):
    """
    class containing projects' objects
    """
    profile_pic = models.ImageField(upload_to='profilepics/', blank=True)
    bio = models.TextField(max_length=80, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        """
        function returns informal representations of the models' objects
        """
        return f'{self.user.username} Profile'