from rest_framework import serializers
from .models import User,Audio,AudioSegment,TextSpeach,CharSet



#User data serialized
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        editorUser = UserSerializer()
        model = Audio
        fields = '__all__'


class AudioSegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioSegment
        sourceAudio = AudioSerializer()
        fields = [
            'id',
            'name',
            'path',
            'sourceAudio',
            'state',
        ]


class TextSpeachSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextSpeach
        fields = '__all__'


class CharSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharSet
        fields = '__all__'