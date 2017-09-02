from django.db import models
from django.utils import timezone

# modelo de la tabla posts.
class Post(models.Model):
    author = models.ForeignKey('auth.User') # autor
    title = models.CharField(max_length=200) # titulo
    text = models.TextField() # texto del post
    category = models.CharField(max_length=200, default='General') # categoria
    created_date = models.DateTimeField(default=timezone.now) # fecha de creacion
    published_date = models.DateTimeField(blank=True, null=True) # fecha de publicacion

    # metodo publicar
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # motodo para obtener titulo
    def __str__(self):
        return self.title

# modelo de la tabla comentarios
class Comment(models.Model):
    author = models.ForeignKey('auth.User') # id del autor
    postid = models.ForeignKey('Post') # id del post
    text = models.TextField(max_length=2048) # contenido del comentarios
    created_date = models.DateTimeField(default=timezone.now) # fecha de creacion
    published_date = models.DateTimeField(blank=True, null=True) # fecha de publicacion

    # metodo publicar
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    # motodo para obtener titulo
    def __str__(self):
        return self.text

    # motodo para obtener titulo
    # def __str__(self):
    #     return self.title
