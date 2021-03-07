from rest_framework import serializers
from snippets.models import Post, Cat
from django.contrib.auth.models import User


class CatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cat
        fields = ['id', 'title', 'root', 'parent_id', 'posts', 'url']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    cat = serializers.ReadOnlyField(source='cat.title')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'url', 'owner', 'cat']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'posts']


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])

        user.save()
        return user
