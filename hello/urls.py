from django.urls import path
from hello.views import hello


urlpatterns = [
    path("", hello, name="hello")
]
