from django.urls import path

from .views import ImageView, CommentView, ImageManipulationView, CommentManipulationView, ImagesStatView

urlpatterns = [
    path('images/<int:image_id>/comments/<int:pk>', CommentManipulationView.as_view()),
    path('images/<int:image_id>/comments/', CommentView.as_view()),
    path('images/stat', ImagesStatView.as_view()),
    path('images/<int:pk>', ImageManipulationView.as_view()),
    path('images/', ImageView.as_view()),
]
