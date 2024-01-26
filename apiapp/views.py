from rest_framework.response import Response
from rest_framework.decorators import api_view

#python에서 @으로 시작하는 단어는 decorator라고 하는데 실제 함수를 호출하기 전에
#특정 내용을 삽입해서 함수를 실행합니다.
#GET 요청이 오면 함수를 호출

@api_view(['GET'])
def hello(request):
  return Response("Hello REST API")

from rest_framework import status
from rest_framework.generics import get_object_or_404

from .models import Soccer
from .serializers import SoccerSerializer

#GET과 POST 모두를 처리
@api_view(['GET','POST'])
def soccersAPI(request):
  #GET 방식의 처리 - 조회를 요청하는 경우
  if request.method == 'GET':
    soccers = Soccer.objects.all()
    serializer = SoccerSerializer(soccers, many=True)
    return Response(serializer.data)
  #POST 방식의 처리 - 삽입하는 경우
  elif request.method == 'POST':
    serializer = SoccerSerializer(data=request.data)
    #유효성 검사를 수행해서 통과하면 삽입하고 그렇지않으면
    #실패한 이유를 출력합니다
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET'])
def oneSoccerAPI(request, bid):
  soccer = get_object_or_404(Soccer, bid=bid)
  serializer = SoccerSerializer(soccer)
  return Response(serializer.data)