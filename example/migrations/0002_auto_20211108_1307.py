# Generated by Django 2.2.15 on 2021-11-08 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(max_length=200, null=True, upload_to='files'),
        ),
    ]
