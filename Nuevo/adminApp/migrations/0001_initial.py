# Generated by Django 5.0.2 on 2024-02-17 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('qualifications', models.CharField(max_length=255)),
                ('experience', models.IntegerField()),
                ('skills', models.TextField()),
                ('cultural_fit', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('resume_path', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]