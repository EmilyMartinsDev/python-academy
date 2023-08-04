from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime
# Create your models here.


class Post(models.Model):
    autor = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    conteudo = RichTextUploadingField()
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'blog_post'
