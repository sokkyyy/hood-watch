# Generated by Django 2.2.7 on 2019-12-02 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0013_auto_20191202_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicservice',
            name='hood',
            field=models.CharField(max_length=100),
        ),
    ]
