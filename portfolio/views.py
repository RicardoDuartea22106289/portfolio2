from django.shortcuts import render, redirect

from .forms import PostForm
from portfolio.models import Post, Disciplina, Pessoa, TrabalhoFinalCurso


def home_page_view(request):
    return render(request, 'portfolio/home.html')


def licenciatura_page_view(request):
    context = {'disciplinas': Disciplina.objects.all()}
    return render(request, 'portfolio/licenciatura.html', context)


def formacao_page_view(request):
    return render(request, 'portfolio/formacao.html')


def projetos_page_view(request):
    context = {
        'trabalhos': TrabalhoFinalCurso.objects.all(),
        'Pessoa': Pessoa.objects.all()
    }
    return render(request, 'portfolio/projetos.html', context)


def contactos_page_view(request):
    return render(request, 'portfolio/contactos.html')


def sobreMim_page_view(request):
    return render(request, 'portfolio/sobreMim.html')


def blog_page_view(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'portfolio/blog.html', context)


def sobreMim_page_view(request):
    return render(request, 'portfolio/sobreMim.html')


def novo_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        pessoaTemp = Pessoa
        for pessoa in Pessoa.objects.all():
            if(pessoa.nome == request.POST.get('autor')):
                pessoaTemp = pessoa

        if form.is_valid():
            post = form.save(commit=False)
            post.Pessoa = pessoaTemp
            post.save()
            return redirect('portfolio:blog')
        else:
            print(form.errors)  # Print form errors to the console
    else:
        form = PostForm()

    pessoas = Pessoa.objects.all()
    return render(request, 'portfolio/novoPost.html', {'form': form, 'pessoas': pessoas})