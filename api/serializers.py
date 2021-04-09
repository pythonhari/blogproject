from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post,comment

class PostSerializer(serializers.ModelSerializer):
    owner=serializers.ReadOnlyField(source='owner.username')
    comments=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    class Meta:
        model=Post
        fields=['id','title','description','owner','comments']
class CommentSerializer(serializers.ModelSerializer):
    owner=serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model=comment
        fields=['id','description','owner','post']
class UserSerializer(serializers.ModelSerializer):
    posts=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    comments=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    class Meta:
        model=User
        fields=['id','username','posts','comments']
