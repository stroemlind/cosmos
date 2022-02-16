# Generated by Django 3.2 on 2022-02-16 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0002_post_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='forum.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forum_comment', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
