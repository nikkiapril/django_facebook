# Generated by Django 2.1.2 on 2018-11-12 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0003_try'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trya',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('master', models.CharField(max_length=120)),
                ('writer', models.CharField(max_length=120)),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
