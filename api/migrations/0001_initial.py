# Generated by Django 4.0.1 on 2022-01-18 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.CharField(max_length=250)),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(default=None, max_length=254, unique=True)),
            ],
        ),
    ]
