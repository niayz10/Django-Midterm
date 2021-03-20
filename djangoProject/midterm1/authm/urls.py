from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from authm.views import something

urlpatterns = [
    path('login', obtain_jwt_token),
    # path('something', something)
]