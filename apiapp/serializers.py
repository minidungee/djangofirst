from rest_framework import serializers
from .models import Soccer

class SoccerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Soccer
    #클라이언트에서 입력하는 데이터만 나열
    #아래 나열한 데이터를 입력하면 Soccer클래스의 인스턴스를 자동 생성
    fields = ['bid','title','author','publisheddate']