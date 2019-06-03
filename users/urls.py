from django.urls import path

from users.views import GetAuthToken

urlpatterns = [
    path('obtain/', GetAuthToken.as_view(), name='obtain'),
]
