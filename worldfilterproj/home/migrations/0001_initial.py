# Generated by Django 4.0.2 on 2022-02-04 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_modifieed', models.DateTimeField(auto_now=True)),
                ('file_id', models.CharField(db_index=True, max_length=30, unique=True)),
                ('file', models.FileField(upload_to='uploads')),
                ('result', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
