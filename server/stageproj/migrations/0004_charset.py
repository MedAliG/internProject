# Generated by Django 3.0 on 2019-12-05 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stageproj', '0003_audio_editoruser'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('chars', models.CharField(max_length=200)),
            ],
        ),
    ]
