# Generated by Django 4.2.3 on 2023-08-04 12:34

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='conteudo',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterModelTable(
            name='post',
            table='blog_post',
        ),
    ]
