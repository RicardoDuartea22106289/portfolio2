from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    linkedin = models.URLField(null=True,blank=True)

    def __str__(self):
        return (self.nome)

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField()
    ano_letivo = models.CharField(max_length=100)
    topicos_abordados = models.TextField()
    ranking = models.IntegerField()
    professor = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    pagina_cadeira = models.URLField(blank=True)

    def __str__(self):
        return (self.nome)

class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    ano_realizacao = models.IntegerField()
    cadeira = models.ForeignKey(Disciplina, on_delete=models.CASCADE, null=True, blank=True)
    participantes = models.ManyToManyField(Pessoa)
    repositorio_github = models.URLField(blank=True)
    video_youtube = models.URLField(blank=True)
    tecnologias_usadas = models.CharField(max_length=200)
    competencias = models.CharField(max_length=100)

class TrabalhoFinalCurso(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ManyToManyField(Pessoa)
    orientador = models.ManyToManyField(Pessoa, related_name='orientador')
    ano_realizacao = models.IntegerField()
    sumario = models.TextField()
    resumo = models.CharField(max_length=500)
    relatorio = models.URLField(blank=True)
    repositorio_github = models.URLField(blank=True)
    video_youtube = models.URLField(blank=True)

    def __str__(self):
        return (self.titulo)

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    autor = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return (self.titulo)

class Comptencia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()