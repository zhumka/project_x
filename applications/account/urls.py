from django.urls import path
from . import views
from applications.account.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('register/', RegisterAPIView.as_view()),
    path('user-info/', UserInfoAPIView.as_view(), name='user-info'),
    path('activate/<uuid:activation_code>/', ActivationAPIView.as_view()),
    path('change_password/', ChangePasswordAPIView.as_view()),
    path('forgot_password/', ForgotPasswordAPIView.as_view()),
    path('forgot_password_confirm/', ForgotPasswordConfirmAPIView.as_view()),
    path('owner-apartment/', views.OwnerUserApartmentAPIView.as_view(), name='owner_apartment'),
    path('owner_apartment_info/<str:email>/', OwnerApartmentInfoByEmailView.as_view(), name='owner_apartment_info_by_email'),
    path('test_celery/', send_mail_view)
]
