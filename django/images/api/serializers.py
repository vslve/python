import os

from rest_framework import serializers

from .models import Image, Comment
from .utils import ImageSerializerMixin


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = 'id', 'text'

    def create(self, validated_data):
        image_id = self .context['view'].kwargs.get('image_id')
        validated_data['image'] = Image.objects.get(id=image_id)
        return Comment.objects.create(**validated_data)


class CommentDetailSerializer(serializers.ModelSerializer):
    image_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Comment
        fields = 'id', 'image_id', 'text'

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance


class ImageSerializer(ImageSerializerMixin, serializers.ModelSerializer):
    comments_count = serializers.SerializerMethodField(source='comments')

    class Meta:
        model = Image
        fields = 'id', 'name', 'image', 'comments_count'
        read_only_fields = 'name', 'size', 'id', 'comments_count'
        extra_kwargs = {'image': {'write_only': True}}

    def create(self, validated_data):
        print(validated_data)
        validated_data['name'] = os.path.splitext(validated_data['image'].name)[0]
        validated_data['size'] = validated_data['image'].size
        return Image.objects.create(**validated_data)


class ImageDetailSerializer(ImageSerializerMixin, serializers.ModelSerializer):
    image_source = serializers.ImageField(source='image')
    comments_count = serializers.SerializerMethodField(source='comments')

    class Meta:
        model = Image
        fields = 'id', 'name', 'comments_count', 'size', 'image_source'
        read_only_fields = 'name', 'size', 'id', 'image_source'
        extra_kwargs = {'image': {'write_only': True}}

    def update(self, instance, validated_data):
        instance.image = validated_data.get('image', instance.image)
        instance.name = os.path.splitext(instance.image.name)[0]
        instance.size = instance.image.size
        instance.save()
        return instance
