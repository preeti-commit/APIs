from django.urls import path,include
from .views import RegistrationAPIView
# from rest_framework import routers
# from myapp.views import registration
from . import views
from .views import LoginAPIView,GeneratePDF,VerifyOTPView,ForgotPasswordView,ResetPasswordView

# # app_name='myapp'
#
# # router = routers.DefaultRouter()
# # router.register('user', RegistrationAPIView)
#
#
urlpatterns = [
    # path('', include(router.urls)),
    path('register/', RegistrationAPIView.as_view()), #Registeration
    # path('register/int:pk', views.registration,name='register'),
    path('login/', LoginAPIView.as_view()),
    path('pdf/', GeneratePDF.as_view()),
    path('login', LoginAPIView.as_view()), #Login after otp verification
    path('verify', VerifyOTPView.as_view()), #otp Verify
    path('forgot', ForgotPasswordView.as_view(), name='forgot-password'), #forgot Password
    path('reset', ResetPasswordView.as_view(), name='reset-password'),

    ]