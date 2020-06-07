from django.db import models
from django.contrib.auth.models import User
import datetime as dt


# Create your models here.
class Profile(models.Model):
    """
    class containing projects' objects
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    profile_pic = models.ImageField( default = 'default.jpg',upload_to='profilepics/')
    bio = models.TextField(max_length=80, blank=True)
    contact = models.CharField(max_length =200,blank=True)

    def __str__(self):
        """
        function returns informal representations of the models' objects
        """
        return f'{self.user.username} Profile'

    def save_profile(self):
        """
        method saves entered profiles to the database
        """
        save()

    def update_profile(self, using=None, fields=None, **kwargs):
        """
        method updates saved profile
        """
        if fields is not None:
            fields = set(fields)
            deferred_fields = self.get_deferred_fields()
            if fields.intersection(deferred_fields):
                fields = fields.union(deferred_fields)
        super().refresh_from_db(using, fields, **kwargs)


    def delete_profile(self):
        """
        method deletes entered profiles to the database
        """
        self.delete()


class Projects(models.Model):
    """
    class containing projects' objects
    """
    project_name = models.CharField(max_length=50, blank=True)
    project_image = models.ImageField(upload_to='projectimages/', blank=True)
    description = models.TextField(max_length=300, blank=True)
    github_repo = models.CharField(max_length=150, blank=True)
    url = models.CharField(max_length=50, blank=True)
    project_user = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.project_name

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.description


