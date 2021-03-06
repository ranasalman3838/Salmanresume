# Generated by Django 3.2.3 on 2021-07-11 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycv', '0006_auto_20210710_0505'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_video', models.FileField(null=True, upload_to='')),
                ('project_name', models.CharField(max_length=200)),
                ('project_description', models.TextField()),
                ('project_link', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='My_model',
        ),
    ]
