# Generated by Django 2.2.7 on 2019-11-13 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20)),
                ('texto', models.TextField()),
                ('autor', models.CharField(max_length=100)),
                ('data_plublic', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
