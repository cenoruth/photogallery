# Generated by Django 4.1.5 on 2023-01-19 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0007_alter_photo_uploaded_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='name',
            field=models.TextField(default='placeholder.img'),
        ),
    ]