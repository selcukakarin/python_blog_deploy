from django.db import models
from ckeditor.fields import RichTextField
from tinymce import models as tinymce_models

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="YAZAR")
    title = models.CharField(max_length=50, verbose_name="BAŞLIK")
    content = RichTextField()
    content2 = tinymce_models.HTMLField()
    article_image = models.FileField(blank=True, null=True, verbose_name="Makaleye fotoğraf ekleyin")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Makale", related_name="comments")
    comment_author = models.CharField(max_length=50, verbose_name="İsim")
    comment_content = models.CharField(max_length=200, verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-comment_date']
