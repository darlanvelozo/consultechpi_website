from django.urls import path
from . import views

app_name = 'web_site'

urlpatterns = [
    # Páginas principais
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('servicos/', views.servicos, name='servicos'),
    path('servicos/<slug:slug>/', views.servico_detalhe, name='servico_detalhe'),
    path('projetos/', views.projetos, name='projetos'),
    path('projetos/<slug:slug>/', views.projeto_detalhe, name='projeto_detalhe'),
    path('equipe/', views.equipe, name='equipe'),
    path('tecnologias/', views.tecnologias, name='tecnologias'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.post_detalhe, name='post_detalhe'),
    path('contato/', views.contato, name='contato'),
    path('orcamento/', views.orcamento, name='orcamento'),
    
    # Páginas legais
    path('politica-privacidade/', views.politica_privacidade, name='politica_privacidade'),
    path('termos-uso/', views.termos_uso, name='termos_uso'),
    
    # APIs
    path('api/newsletter/', views.newsletter_inscricao, name='newsletter_inscricao'),
    path('sitemap.xml', views.sitemap, name='sitemap'),
] 