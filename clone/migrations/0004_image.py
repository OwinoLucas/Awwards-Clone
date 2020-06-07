# Generated by Django 3.0.6 on 2020-06-07 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0003_auto_20200607_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
