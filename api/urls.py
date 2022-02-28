from django.urls import path,include
# from .views import RegistrationAPIView
# # from rest_framework import routers
from api.views import RegistrationView
from . import views

# # app_name='myapp'
#
# # router = routers.DefaultRouter()
# # router.register('user', RegistrationAPIView)
#
#
urlpatterns = [
    # path('', include(router.urls)),
    path('registerss/', RegistrationView.as_view())

    ]