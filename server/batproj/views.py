from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from stageproj.models import Audio, AudioSegment, User, TextSpeach, CharSet
from stageproj.serializers import UserSerializer, AudioSerializer, TextSpeachSerializer, AudioSegmentSerializer, CharSetSerializer
import os
from batproj.inputTest import inputTextTest


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    userData = UserSerializer(User.objects.filter(username=username)[0])
    return Response({'token': token.key, 'user_id': userData.data['id'], 'username': username},
                    status=HTTP_200_OK)


'''@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    user = User.objects.get(id=request.data.get())
    output = UserSerializer(user).data
    return Response(output, status=HTTP_200_OK)*/'''


@csrf_exempt
@api_view(["POST"])
def submitData(request):
    querySet = CharSet.objects.all()
    charSetQuery = querySet.reverse()[0]
    charSet1 = CharSetSerializer(charSetQuery).data
    charset = charSet1["chars"]

    textData = request.data.get("text")

    if inputTextTest(charset, textData):
        # getting related audioSegment
        relatedSegmentId = request.data.get("segementId")
        relatedSegment = AudioSegment.objects.get(id=relatedSegmentId)
        relatedSegmentData = AudioSegmentSerializer(relatedSegment).data
        relatedInsert = TextSpeach.objects.filter(segment=relatedSegment)
        if relatedInsert:
            relatedInsertData = TextSpeachSerializer(relatedInsert[0])
            relatedInsert.update(text=textData)
        else:
            dataInsert, created = TextSpeach.objects.get_or_create(
                text=textData, segment=relatedSegment)

        # updating the SegemntTo tranlated

        AudioSegment.objects.filter(id=relatedSegmentId).update(state=1)
        # return Response({"ay":relatedSegmentData},status=HTTP_200_OK)
        relatedAudioId = relatedSegmentData["sourceAudio"]
        userId = request.data.get("userId")
        editorUser = User.objects.filter(id=userId)[0]
        # return Response({"relatedAudioId": relatedAudioId}, status=HTTP_200_OK)
        relatedAudio = Audio.objects.get(id=relatedAudioId)
        relatedAudioData = AudioSerializer(relatedAudio).data
        # return Response({"i stopped here": relatedAudioData}, status=HTTP_200_OK)
        finishTest = False
        segmentsQuery = AudioSegment.objects.filter(
            sourceAudio=relatedAudioData["id"])
        segmentsData = AudioSegmentSerializer(segmentsQuery, many=True).data
        # return Response({"relatedSegements":segmentsData},status=HTTP_200_OK)
        state = 2
        for sgment in segmentsData:
            if sgment["state"] == 0:
                segState = 1
            else:
                segState = 2

        Audio.objects.filter(id=relatedAudioId).update(
            state=segState, editorUser=editorUser)

        return Response({'text': textData}, status=HTTP_200_OK)
    else:
        return Response({'error': 'Submitted text does not respect the input rules'}, status=HTTP_400_BAD_REQUEST)


'''@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def audioFile(request):
    #i need to finish this 
    dirpath = os.getcwd()
    fname = request.query_params.get("name")
    foldername = os.path.basename(dirpath)
    fpath = "server\\stageproj\\data\\"+fname
    f = open(fpath,"rb") 
    response = HttpResponse()
    response.write(f.read())
    response['Content-Type'] ='audio/mp3'
    response['Content-Length'] =os.path.getsize(fname )
    return response
'''
@csrf_exempt
@api_view(["GET"])
def getUserAudio(request):
    querySet = Audio.objects.filter(
        editorUser__id=request.query_params.get('id'))
    if querySet:
        output = AudioSerializer(querySet, many=True).data
        return Response(output, status=HTTP_200_OK)
    else:
        return Response({"error": "Parametre given is wrong."}, status=HTTP_404_NOT_FOUND)


@csrf_exempt
@api_view(["GET"])
def getAudioSegmentData(request):
    querySet = AudioSegment.objects.filter(
        sourceAudio__id=request.query_params.get('id'))
    if querySet:

        output = AudioSegmentSerializer(querySet, many=True).data

        return Response(output, status=HTTP_200_OK)
    else:
        return Response({"error": "Data with submitted id doesn't figure in the database"}, status=HTTP_404_NOT_FOUND)


@csrf_exempt
@api_view(['GET'])
def getSegmentData(request):
    segmentid = request.query_params.get("id")
    querySet = AudioSegment.objects.filter(id=segmentid)

    if querySet:
        audioData = AudioSegmentSerializer(querySet[0])
        querySet = AudioSegment.objects.get(id=segmentid)
        # return Response({"id": audioData.data}, status=HTTP_200_OK)

        querySet2 = TextSpeach.objects.filter(
            segment=querySet)

        if not querySet2:
            output = {
                "audio": audioData.data,
                "text": ""
            }
        else:
            TextData = TextSpeachSerializer(querySet2[0])
            output = {
                "audio": audioData.data,
                "text": TextData.data
            }
        return Response(output, status=HTTP_200_OK)
    else:
        return Response({"error": "id provided doesn't exist !"})


@csrf_exempt
@api_view(["GET"])
def getSegmentText(request):

    querySet = TextSpeach.objects.filter(
        segment__id=request.query_params.get('id'))

    if querySet:
        output = TextSpeachSerializer(querySet, many=True).data
        return Response(output, status=HTTP_200_OK)
    else:
        return Response({"error": "id provided doesn't exist !"})
