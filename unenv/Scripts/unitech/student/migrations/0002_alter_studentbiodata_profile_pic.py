# Generated by Django 4.2.4 on 2023-08-18 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentbiodata',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pic/Student/'),
        ),
    ]
