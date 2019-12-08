from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth import get_user_model

class User(User):
    class Meta:
        proxy = True
        ordering = ('first_name', )
    def str(self):
        return self.first_name+" "+self.last_name
    def fullName(self):
        return self.first_name+" "+self.last_name
#User = get_user_model()

class Audio(models.Model):
    name = models.CharField(max_length=50)
    path = models.FileField(upload_to='media/data/')
    state = models.IntegerField(default=0)
    editorUser = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    def  __str__(self):
        return self.name

class AudioSegment(models.Model):
    name = models.CharField(max_length=50)
    path = models.FileField(max_length=50)
    sourceAudio = models.ForeignKey(Audio,on_delete=models.CASCADE,blank=False, null=False)
    state = models.IntegerField(default=0)
    def  __str__(self):
        return self.name

class TextSpeach(models.Model):
    text = models.CharField(max_length=400)
    segment = models.ForeignKey(AudioSegment,on_delete=models.CASCADE,blank=False, null=False)
    def  __str__(self):
        return self.text

class CharSet(models.Model):
    title = models.CharField(max_length = 50)
    chars = models.CharField(max_length = 200)