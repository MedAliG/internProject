from rest_framework import viewsets
from .models import User, Audio, AudioSegment, TextSpeach, CharSet
from .serializers import UserSerializer, AudioSerializer, AudioSegmentSerializer, TextSpeachSerializer, CharSetSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AudioViewSet(viewsets.ModelViewSet):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer


class AudioSegmentViewSet(viewsets.ModelViewSet):
    queryset = AudioSegment.objects.all()
    serializer_class = AudioSegmentSerializer


class AudioSegmentFilterViewSet(viewsets.ModelViewSet):
    queryset = AudioSegment.objects.filter()
    serializer_class = AudioSegmentSerializer


class TextSpeachViewSet(viewsets.ModelViewSet):
    queryset = TextSpeach.objects.all()
    serializer_class = TextSpeachSerializer


class CharSetViewSet(viewsets.ModelViewSet):
    queryset = CharSet.objects.all()
    serializer_class = CharSetSerializer
