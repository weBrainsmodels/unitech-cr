# Generated by Django 4.2.4 on 2023-09-07 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_Code', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Course Code',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_Title', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Course',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Department',
            },
        ),
        migrations.CreateModel(
            name='CreateQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_Question', models.CharField(max_length=200)),
                ('option_A', models.CharField(max_length=200)),
                ('option_B', models.CharField(max_length=200)),
                ('option_C', models.CharField(max_length=200)),
                ('option_D', models.CharField(max_length=200)),
                ('marks', models.CharField(max_length=200)),
                ('correct_Answer', models.CharField(max_length=200)),
                ('course_Code', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='QuestionBank.course')),
                ('course_title', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='QuestionBank.code')),
                ('name', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='QuestionBank.department')),
            ],
            options={
                'verbose_name_plural': 'Question Bank',
            },
        ),
    ]