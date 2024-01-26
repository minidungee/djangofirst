from django.urls import path
from .views import hello, soccersAPI, oneSoccerAPI

#python에서 @으로 시작하는 단어는 decorator라고 하는데 실제 함수를 호출하기 전에
#특정 내용을 삽입해서 함수를 실행합니다.
#GET 요청이 오면 함수를 호출

urlpatterns = [
  path("hello/", hello),
  path("soccers/", soccersAPI),
  path("soccer/<int:bid>", oneSoccerAPI),
]
# 나는 최고다