from django.contrib import admin
from .models import Post
from catalogo.models import Produto,Categoria
from core.models import Curso

admin.site.register(Post)
admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Curso)
# Register your models here.
