from django.urls import path
from .views import hello, soccersAPI, oneSoccerAPI


urlpatterns = [
  path("hello/", hello),
  path("soccers/", soccersAPI),
  path("soccer/<int:bid>", oneSoccerAPI),
]
# 나는 최고다