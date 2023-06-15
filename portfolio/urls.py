from django.shortcuts import render

from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('formacao', views.formacao_page_view, name='formacao'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('contactos', views.contactos_page_view, name='contactos'),
    path('sobreMim', views.sobreMim_page_view, name='sobreMim'),
    path('blog', views.blog_page_view, name='blog'),
    path('novo_post', views.novo_post, name='novoPost'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)