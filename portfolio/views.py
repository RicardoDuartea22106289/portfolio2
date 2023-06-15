from django.shortcuts import render

from .models import Post, Disciplina


def home_page_view(request):
	return render(request, 'portfolio/home.html')

def licenciatura_page_view(request):
	context = {'disciplinas': Disciplina.objects.all()}
	return render(request, 'portfolio/licenciatura.html',context)

def formacao_page_view(request):
	return render(request, 'portfolio/formacao.html')

def projetos_page_view(request):
	return render(request, 'portfolio/projetos.html')

def contactos_page_view(request):
	return render(request, 'portfolio/contactos.html')

def sobreMim_page_view(request):
	return render(request, 'portfolio/sobreMim.html')

def blog_page_view(request):
	context = {'posts': Post.objects.all()}
	return render(request, 'portfolio/blog.html', context)