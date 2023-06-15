from django.contrib import admin
from .models import Disciplina, Pessoa, Projeto, TrabalhoFinalCurso, Post

admin.site.register(Disciplina)
admin.site.register(Pessoa)
admin.site.register(Projeto)
admin.site.register(TrabalhoFinalCurso)
admin.site.register(Post)