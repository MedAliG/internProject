from django.contrib import admin
from .models import Audio,User,AudioSegment,TextSpeach,CharSet

admin.site.register(Audio)
admin.site.register(AudioSegment)
admin.site.register(User)
admin.site.register(TextSpeach)
admin.site.register(CharSet)


