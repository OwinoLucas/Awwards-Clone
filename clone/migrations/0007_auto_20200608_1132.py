# Generated by Django 3.0.6 on 2020-06-08 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0006_auto_20200607_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='project_image',
            field=models.ImageField(upload_to='projectimages/'),
        ),
    ]
