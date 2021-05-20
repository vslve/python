from rest_framework import generics

from api.models import Comment, Image


class CommentMixin:
    serializer_class = None

    def get_queryset(self):
        image_id = self.kwargs['image_id']
        generics.get_object_or_404(Image.objects.all(), id=image_id)
        return Comment.objects.all().filter(image_id=image_id)


class ImageSerializerMixin:

    def get_comments_count(self, instance):
        return Comment.objects.all().filter(image_id=instance.id).count()

