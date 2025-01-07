from rest_framework.serializers import ModelSerializer
from .models import Note
from rest_framework import serializers
from tasks.models import Task
from django.contrib.auth.models import User

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "title", "description", "done", "created_at")
        read_only_fields = ("id","created_at")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        
        extra_kwargs = {"password": { "required": True}}
        extra_kwargs = {"email": {"required": True}}
        extra_kwargs = {"username": {"required": True}}
        unique_together = ["username", "email"]
        read_only_fields = ["id"]
        
    def validate(self, data):
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError({"username": "This username is already exist."})
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({"email": "This email is already exist."})
        return data