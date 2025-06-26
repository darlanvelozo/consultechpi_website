from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import (
    CategoriaServico, Servico, Tecnologia, Projeto, MembroEquipe,
    Depoimento, BlogPost, Contato, ConfiguracaoSite, Newsletter
)

@admin.register(CategoriaServico)
class CategoriaServicoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ordem', 'ativo', 'data_criacao']
    list_editable = ['ordem', 'ativo']
    list_filter = ['ativo', 'data_criacao']
    search_fields = ['nome', 'descricao']
    ordering = ['ordem', 'nome']

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'preco_inicial', 'destaque', 'ativo', 'data_criacao']
    list_editable = ['destaque', 'ativo']
    list_filter = ['categoria', 'destaque', 'ativo', 'data_criacao']
    search_fields = ['nome', 'descricao_curta', 'descricao_completa']
    prepopulated_fields = {'slug': ('nome',)}
    readonly_fields = ['data_criacao', 'data_atualizacao']
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('categoria', 'nome', 'slug', 'descricao_curta', 'descricao_completa')
        }),
        ('Detalhes Técnicos', {
            'fields': ('caracteristicas', 'tecnologias', 'tempo_estimado', 'preco_inicial')
        }),
        ('Mídia', {
            'fields': ('imagem',)
        }),
        ('Configurações', {
            'fields': ('destaque', 'ativo')
        }),
        ('Datas', {
            'fields': ('data_criacao', 'data_atualizacao'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo', 'nivel_expertise', 'anos_experiencia', 'ativo']
    list_editable = ['nivel_expertise', 'anos_experiencia', 'ativo']
    list_filter = ['tipo', 'ativo', 'data_criacao']
    search_fields = ['nome', 'descricao']
    ordering = ['tipo', 'nivel_expertise']

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cliente', 'status', 'data_inicio', 'destaque', 'ativo']
    list_editable = ['status', 'destaque', 'ativo']
    list_filter = ['status', 'categoria_servico', 'destaque', 'ativo', 'data_inicio']
    search_fields = ['nome', 'cliente', 'descricao']
    prepopulated_fields = {'slug': ('nome',)}
    filter_horizontal = ['tecnologias']
    readonly_fields = ['data_criacao']
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'slug', 'cliente', 'descricao')
        }),
        ('Detalhes Técnicos', {
            'fields': ('desafios', 'solucoes', 'tecnologias', 'categoria_servico')
        }),
        ('Mídia e Links', {
            'fields': ('imagem_principal', 'imagens_adicionais', 'url_projeto', 'url_github')
        }),
        ('Datas e Status', {
            'fields': ('data_inicio', 'data_conclusao', 'status')
        }),
        ('Configurações', {
            'fields': ('destaque', 'ativo')
        }),
    )

@admin.register(MembroEquipe)
class MembroEquipeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cargo', 'anos_experiencia', 'destaque', 'ativo']
    list_editable = ['cargo', 'anos_experiencia', 'destaque', 'ativo']
    list_filter = ['cargo', 'destaque', 'ativo', 'data_entrada']
    search_fields = ['nome', 'bio', 'especialidades']
    filter_horizontal = ['tecnologias']
    readonly_fields = ['data_criacao']
    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('nome', 'cargo', 'bio', 'foto')
        }),
        ('Especialidades', {
            'fields': ('especialidades', 'tecnologias', 'anos_experiencia')
        }),
        ('Redes Sociais', {
            'fields': ('linkedin', 'github', 'email')
        }),
        ('Configurações', {
            'fields': ('destaque', 'ativo', 'data_entrada')
        }),
    )

@admin.register(Depoimento)
class DepoimentoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'empresa', 'avaliacao', 'destaque', 'ativo', 'data_criacao']
    list_editable = ['avaliacao', 'destaque', 'ativo']
    list_filter = ['avaliacao', 'destaque', 'ativo', 'data_criacao']
    search_fields = ['cliente', 'empresa', 'depoimento']
    readonly_fields = ['data_criacao']
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('projeto_relacionado')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'visualizacoes', 'tempo_leitura', 'publicado', 'destaque', 'data_publicacao']
    list_editable = ['publicado', 'destaque', 'visualizacoes']
    list_filter = ['publicado', 'destaque', 'data_publicacao', 'data_criacao']
    search_fields = ['titulo', 'resumo', 'conteudo']
    prepopulated_fields = {'slug': ('titulo',)}
    filter_horizontal = ['tecnologias_relacionadas']
    readonly_fields = ['data_criacao', 'data_atualizacao']
    fieldsets = (
        ('Conteúdo', {
            'fields': ('titulo', 'slug', 'resumo', 'conteudo', 'imagem_destaque')
        }),
        ('Metadados', {
            'fields': ('autor', 'tags', 'tecnologias_relacionadas', 'tempo_leitura')
        }),
        ('Estatísticas', {
            'fields': ('visualizacoes',)
        }),
        ('Configurações', {
            'fields': ('destaque', 'publicado', 'data_publicacao')
        }),
        ('Datas', {
            'fields': ('data_criacao', 'data_atualizacao'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'tipo_contato', 'assunto', 'lido', 'respondido', 'data_criacao']
    list_editable = ['lido', 'respondido']
    list_filter = ['tipo_contato', 'lido', 'respondido', 'data_criacao']
    search_fields = ['nome', 'email', 'assunto', 'mensagem']
    readonly_fields = ['data_criacao']
    actions = ['marcar_como_lido', 'marcar_como_respondido']
    
    def marcar_como_lido(self, request, queryset):
        queryset.update(lido=True)
    marcar_como_lido.short_description = "Marcar como lido"
    
    def marcar_como_respondido(self, request, queryset):
        queryset.update(respondido=True)
    marcar_como_respondido.short_description = "Marcar como respondido"

@admin.register(ConfiguracaoSite)
class ConfiguracaoSiteAdmin(admin.ModelAdmin):
    list_display = ['nome_empresa', 'email_contato', 'telefone', 'data_atualizacao']
    readonly_fields = ['data_atualizacao']
    
    def has_add_permission(self, request):
        # Permite apenas uma configuração
        return not ConfiguracaoSite.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # Não permite deletar a configuração
        return False

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email', 'nome', 'ativo', 'data_inscricao']
    list_editable = ['ativo']
    list_filter = ['ativo', 'data_inscricao']
    search_fields = ['email', 'nome']
    readonly_fields = ['data_inscricao']
    actions = ['ativar_newsletter', 'desativar_newsletter']
    
    def ativar_newsletter(self, request, queryset):
        queryset.update(ativo=True)
    ativar_newsletter.short_description = "Ativar newsletter"
    
    def desativar_newsletter(self, request, queryset):
        queryset.update(ativo=False)
    desativar_newsletter.short_description = "Desativar newsletter"

# Configurações do Admin
admin.site.site_header = "ConsulTechPI - Administração"
admin.site.site_title = "ConsulTechPI Admin"
admin.site.index_title = "Bem-vindo ao Painel Administrativo"
