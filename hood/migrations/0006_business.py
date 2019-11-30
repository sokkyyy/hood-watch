# Generated by Django 2.2.7 on 2019-11-30 07:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0005_user_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=240)),
                ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='businesses', to='hood.Hood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='businesses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]