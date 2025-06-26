from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import json

from .models import (
    CategoriaServico, Servico, Tecnologia, Projeto, MembroEquipe,
    Depoimento, BlogPost, Contato, ConfiguracaoSite, Newsletter
)
from .forms import ContatoForm, NewsletterForm

def home(request):
    """Página inicial do site"""
    # Buscar configuração do site ou criar uma padrão
    config = ConfiguracaoSite.objects.first()
    if not config:
        # Criar configuração padrão se não existir
        config = ConfiguracaoSite.objects.create(
            nome_empresa="ConsulTech Piauí",
            slogan="Transformando ideias em soluções tecnológicas inovadoras",
            descricao_empresa="Somos uma consultoria tecnológica especializada em desenvolvimento de sites, sistemas e automação no Piauí.",
            email_contato="contato@consultechpiaui.com",
            telefone="(86) 99999-9999",
            whatsapp="(86) 99999-9999",
            endereco="Teresina, Piauí - Brasil",
            meta_description="Consultoria tecnológica especializada em desenvolvimento de sites, sistemas e automação no Piauí.",
            meta_keywords="consultoria tecnológica, desenvolvimento web, sistemas, automação, Piauí, Teresina",
            mostrar_servicos=True,
            mostrar_sobre=True,
            mostrar_portfolio=True,
        )
    
    context = {
        'config': config,
        'servicos_destaque': Servico.objects.filter(destaque=True, ativo=True)[:6],
        'projetos_destaque': Projeto.objects.filter(destaque=True, ativo=True)[:4],
        'depoimentos_destaque': Depoimento.objects.filter(destaque=True, ativo=True)[:3],
        'equipe_destaque': MembroEquipe.objects.filter(destaque=True, ativo=True)[:4],
        'tecnologias_destaque': Tecnologia.objects.filter(ativo=True).order_by('-nivel_expertise')[:8],
        'posts_recentes': BlogPost.objects.filter(publicado=True).order_by('-data_publicacao')[:3],
        'estatisticas': {
            'projetos_concluidos': Projeto.objects.filter(status='concluido').count(),
            'clientes_atendidos': Projeto.objects.values('cliente').distinct().count(),
            'anos_experiencia': 5,  # ajuste conforme necessário ou calcule dinamicamente
            'tecnologias_dominadas': Tecnologia.objects.filter(nivel_expertise__gte=8).count(),
        },
    }
    return render(request, 'web_site/home.html', context)

def sobre(request):
    """Página sobre a empresa"""
    config = ConfiguracaoSite.objects.first()
    context = {
        'config': config,
        'equipe': MembroEquipe.objects.filter(ativo=True).order_by('cargo', 'nome'),
        'tecnologias': Tecnologia.objects.filter(ativo=True).order_by('tipo', '-nivel_expertise'),
        'estatisticas': {
            'projetos_concluidos': Projeto.objects.filter(status='concluido').count(),
            'clientes_atendidos': Projeto.objects.values('cliente').distinct().count(),
            'anos_experiencia': 5,  # Ajustar conforme necessário
            'tecnologias_dominadas': Tecnologia.objects.filter(nivel_expertise__gte=8).count(),
        }
    }
    return render(request, 'web_site/sobre.html', context)

def servicos(request):
    """Lista de todos os serviços"""
    config = ConfiguracaoSite.objects.first()
    categorias = CategoriaServico.objects.filter(ativo=True).prefetch_related('servicos')
    context = {
        'config': config,
        'categorias': categorias,
        'servicos_todos': Servico.objects.filter(ativo=True),
    }
    return render(request, 'web_site/servicos.html', context)

def servico_detalhe(request, slug):
    """Detalhes de um serviço específico"""
    config = ConfiguracaoSite.objects.first()
    servico = get_object_or_404(Servico, slug=slug, ativo=True)
    servicos_relacionados = Servico.objects.filter(
        categoria=servico.categoria, ativo=True
    ).exclude(id=servico.id)[:3]
    
    context = {
        'config': config,
        'servico': servico,
        'servicos_relacionados': servicos_relacionados,
    }
    return render(request, 'web_site/servico_detalhe.html', context)

def projetos(request):
    """Lista de todos os projetos"""
    config = ConfiguracaoSite.objects.first()
    projetos_list = Projeto.objects.filter(ativo=True).prefetch_related('tecnologias')
    
    # Filtros
    categoria = request.GET.get('categoria')
    status = request.GET.get('status')
    tecnologia = request.GET.get('tecnologia')
    
    if categoria:
        projetos_list = projetos_list.filter(categoria_servico__slug=categoria)
    if status:
        projetos_list = projetos_list.filter(status=status)
    if tecnologia:
        projetos_list = projetos_list.filter(tecnologias__nome__icontains=tecnologia)
    
    # Paginação
    paginator = Paginator(projetos_list, 9)
    page_number = request.GET.get('page')
    projetos_paginados = paginator.get_page(page_number)
    
    context = {
        'config': config,
        'projetos': projetos_paginados,
        'categorias': CategoriaServico.objects.filter(ativo=True),
        'tecnologias': Tecnologia.objects.filter(ativo=True),
        'filtros': {
            'categoria': categoria,
            'status': status,
            'tecnologia': tecnologia,
        }
    }
    return render(request, 'web_site/projetos.html', context)

def projeto_detalhe(request, slug):
    """Detalhes de um projeto específico"""
    config = ConfiguracaoSite.objects.first()
    projeto = get_object_or_404(Projeto, slug=slug, ativo=True)
    projetos_relacionados = Projeto.objects.filter(
        categoria_servico=projeto.categoria_servico, ativo=True
    ).exclude(id=projeto.id)[:3]
    
    context = {
        'config': config,
        'projeto': projeto,
        'projetos_relacionados': projetos_relacionados,
    }
    return render(request, 'web_site/projeto_detalhe.html', context)

def equipe(request):
    """Página da equipe"""
    config = ConfiguracaoSite.objects.first()
    context = {
        'config': config,
        'equipe': MembroEquipe.objects.filter(ativo=True).order_by('cargo', 'nome'),
        'cargos': MembroEquipe.CARGO_CHOICES,
    }
    return render(request, 'web_site/equipe.html', context)

def tecnologias(request):
    """Página de tecnologias"""
    config = ConfiguracaoSite.objects.first()
    tecnologias_por_tipo = {}
    for tipo, nome_tipo in Tecnologia.TIPO_CHOICES:
        tecnologias_por_tipo[nome_tipo] = Tecnologia.objects.filter(
            tipo=tipo, ativo=True
        ).order_by('-nivel_expertise')
    
    context = {
        'config': config,
        'tecnologias_por_tipo': tecnologias_por_tipo,
        'tipos': Tecnologia.TIPO_CHOICES,
    }
    return render(request, 'web_site/tecnologias.html', context)

def blog(request):
    """Lista de posts do blog"""
    config = ConfiguracaoSite.objects.first()
    posts_list = BlogPost.objects.filter(publicado=True).select_related('autor')
    
    # Filtros
    tag = request.GET.get('tag')
    tecnologia = request.GET.get('tecnologia')
    autor = request.GET.get('autor')
    
    if tag:
        posts_list = posts_list.filter(tags__contains=[tag])
    if tecnologia:
        posts_list = posts_list.filter(tecnologias_relacionadas__nome__icontains=tecnologia)
    if autor:
        posts_list = posts_list.filter(autor__nome__icontains=autor)
    
    # Busca
    q = request.GET.get('q')
    if q:
        posts_list = posts_list.filter(
            Q(titulo__icontains=q) | 
            Q(resumo__icontains=q) | 
            Q(conteudo__icontains=q)
        )
    
    # Paginação
    paginator = Paginator(posts_list, 6)
    page_number = request.GET.get('page')
    posts_paginados = paginator.get_page(page_number)
    
    context = {
        'config': config,
        'posts': posts_paginados,
        'autores': MembroEquipe.objects.filter(ativo=True),
        'tecnologias': Tecnologia.objects.filter(ativo=True),
        'filtros': {
            'tag': tag,
            'tecnologia': tecnologia,
            'autor': autor,
            'q': q,
        }
    }
    return render(request, 'web_site/blog.html', context)

def post_detalhe(request, slug):
    """Detalhes de um post do blog"""
    config = ConfiguracaoSite.objects.first()
    post = get_object_or_404(BlogPost, slug=slug, publicado=True)
    
    # Incrementar visualizações
    post.visualizacoes += 1
    post.save()
    
    posts_relacionados = BlogPost.objects.filter(
        publicado=True
    ).exclude(id=post.id)[:3]
    
    context = {
        'config': config,
        'post': post,
        'posts_relacionados': posts_relacionados,
    }
    return render(request, 'web_site/post_detalhe.html', context)

def contato(request):
    """Página de contato"""
    config = ConfiguracaoSite.objects.first()
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            contato = form.save()
            messages.success(request, 'Mensagem enviada com sucesso! Entraremos em contato em breve.')
            return redirect('web_site:contato')
    else:
        form = ContatoForm()
    
    context = {
        'config': config,
        'form': form,
    }
    return render(request, 'web_site/contato.html', context)

@csrf_exempt
def newsletter_inscricao(request):
    """API para inscrição na newsletter"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            nome = data.get('nome', '')
            
            if email:
                newsletter, created = Newsletter.objects.get_or_create(
                    email=email,
                    defaults={'nome': nome}
                )
                
                if created:
                    return JsonResponse({
                        'success': True,
                        'message': 'Inscrição realizada com sucesso!'
                    })
                else:
                    return JsonResponse({
                        'success': False,
                        'message': 'Este email já está inscrito.'
                    })
            else:
                return JsonResponse({
                    'success': False,
                    'message': 'Email é obrigatório.'
                })
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'message': 'Dados inválidos.'
            })
    
    return JsonResponse({
        'success': False,
        'message': 'Método não permitido.'
    })

def orcamento(request):
    """Página de orçamento"""
    config = ConfiguracaoSite.objects.first()
    servicos = Servico.objects.filter(ativo=True)
    
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            contato = form.save(commit=False)
            contato.tipo_contato = 'orcamento'
            contato.save()
            messages.success(request, 'Solicitação de orçamento enviada! Analisaremos e entraremos em contato.')
            return redirect('web_site:orcamento')
    else:
        form = ContatoForm()
    
    context = {
        'config': config,
        'form': form,
        'servicos': servicos,
    }
    return render(request, 'web_site/orcamento.html', context)

def politica_privacidade(request):
    """Página de política de privacidade"""
    config = ConfiguracaoSite.objects.first()
    context = {
        'config': config,
    }
    return render(request, 'web_site/politica_privacidade.html', context)

def termos_uso(request):
    """Página de termos de uso"""
    config = ConfiguracaoSite.objects.first()
    context = {
        'config': config,
    }
    return render(request, 'web_site/termos_uso.html', context)

def sitemap(request):
    """Sitemap XML para SEO"""
    from django.http import HttpResponse
    from django.template.loader import render_to_string
    
    context = {
        'projetos': Projeto.objects.filter(ativo=True),
        'posts': BlogPost.objects.filter(publicado=True),
        'servicos': Servico.objects.filter(ativo=True),
    }
    
    xml = render_to_string('web_site/sitemap.xml', context)
    return HttpResponse(xml, content_type='application/xml')
