"""batproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import login,submitData,getSegmentData,getAudioSegmentData,getUserAudio,getSegmentText
from .routers import router
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/audio',audioGetAll),
    path('segment/', getAudioSegmentData),
    path('getUserAudio/', getUserAudio),
    path('textToSpeach/', getSegmentText),
    path('textData/',submitData),
    path('seg/', getSegmentData),
    #path('audioFile/', audioFile),
    path('api/', include(router.urls)),
    path('login', login),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



#path('api/', include(router.urls)),