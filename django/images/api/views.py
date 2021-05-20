from rest_framework import generics, status
from rest_framework.response import Response

from .models import Image, Comment
from .serializers import ImageSerializer, ImageDetailSerializer, CommentDetailSerializer, CommentSerializer
from .utils import CommentMixin


class ImageView(generics.ListCreateAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()


class ImageManipulationView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ImageDetailSerializer
    queryset = Image.objects.all()


class CommentView(CommentMixin, generics.ListCreateAPIView):
    serializer_class = CommentSerializer


class CommentManipulationView(CommentMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentDetailSerializer


class ImagesStatView(generics.ListAPIView):

    def get(self, request, *args, **kwargs):
        total_images = Image.objects.count()
        total_unique_images = Image.objects.all().distinct('name').count()
        total_comments = Comment.objects.count()
        total_unique_comments = Comment.objects.all().distinct('text').count()
        total_size = sum(map(lambda img: img.size, Image.objects.all()))

        return Response({
            'total_images': total_images,
            'total_unique_images': total_unique_images,
            'total_comments': total_comments,
            'total_unique_comments': total_unique_comments,
            'total_size': total_size
            }, status=status.HTTP_200_OK
        )
