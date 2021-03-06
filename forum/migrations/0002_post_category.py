# Generated by Django 3.2 on 2022-02-16 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('New Releases', 'New Releases'), ('Album Review', 'Album Review'), ('Music Video', 'Music Video'), ('Afro', 'Afro'), ('Blues', 'Blues'), ('Christmas', 'Christmas'), ('Classic', 'Classic'), ('Country', 'Country'), ('Disco', 'Disco'), ('EDM', 'EDM'), ('Folk', 'Folk'), ('Funk', 'Funk'), ('HipHop', 'HipHop'), ('Indie', 'Indie'), ('Jazz', 'Jazz'), ('K-Pop', 'K-Pop'), ('Latino', 'Latino'), ('Metal', 'Metal'), ('Pop', 'Pop'), ('Punk', 'Punk'), ('Rap', 'Rap'), ('Reggae', 'Reggae'), ('RnB', 'RnB'), ('Rock', 'Rock'), ('Soul', 'Soul')], default='none', max_length=40),
        ),
    ]
