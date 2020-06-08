from rest_framework import serializers
from .models import Events,Profile,Projects

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('id', 'event', 'description', 'price')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ( 'user', 'profile_pic', 'bio','contact')

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ( 'project_name','project_image', 'description', 'github_repo','url','project_user','created_at')