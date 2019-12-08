from rest_framework import routers
from stageproj.viewsets import UserViewSet, AudioSegmentFilterViewSet, AudioViewSet, TextSpeachViewSet, AudioSegmentViewSet, CharSetViewSet

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('audio', AudioViewSet)
router.register('textspeach', TextSpeachViewSet)
router.register('audioSegmnt', AudioSegmentViewSet)
router.register('audioSegmntFilter', AudioSegmentFilterViewSet)
router.register('charset', CharSetViewSet)
