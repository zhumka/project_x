from django.urls import path, include
from . import views
from applications.apartment.views import *
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()

router.register('category', CategoryModelViewSet)
router.register('comments', CommentModelViewSet)
router.register('image', ImageModelViewSet)
router.register('', ApartmentAPIVIew, basename='apartment')

urlpatterns = [
    path('get/<str:name>/', UserActionHistoryAPIView.as_view(), name='user-action-history'),
    path('recommendations/', views.ApartmentAPIVIew.as_view({'get': 'get_recommendations'}),
         name='apartment-recommendations'),
]

urlpatterns += router.urls

