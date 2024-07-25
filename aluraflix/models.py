from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Categoria(models.Model):
    titulo = models.CharField(max_length=50)
    cor = models.CharField(max_length=9)

    def __str__(self):
        return self.titulo

class Video(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=400)
    url = models.URLField(max_length=200)
    categoria = models.ManyToManyField(Categoria, blank=True)

    def __str__(self):
        return self.titulo
    
@receiver(post_save, sender=Video)
def set_default_categoria(sender, instance, created, **kwargs):
    if created and not instance.categoria.exists():
        default_categoria= Categoria.objects.get_or_create(id=1, defaults={'titulo': 'Livre', 'cor': '#000'})[0]
        instance.categoria.add(default_categoria)