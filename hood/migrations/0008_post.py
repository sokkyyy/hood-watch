# Generated by Django 2.2.7 on 2019-11-30 12:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0007_publicservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=240)),
                ('description', models.TextField()),
                ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='hood.Hood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
