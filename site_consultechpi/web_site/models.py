from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
import uuid

class CategoriaServico(models.Model):
    """Categorias de serviços oferecidos pela consultoria"""
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField()
    icone = models.CharField(max_length=50, help_text="Classe do ícone (ex: fas fa-code)")
    ordem = models.PositiveIntegerField(default=0)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['ordem', 'nome']
        verbose_name = "Categoria de Serviço"
        verbose_name_plural = "Categorias de Serviços"
    
    def __str__(self):
        return self.nome

class Servico(models.Model):
    """Serviços oferecidos pela consultoria"""
    categoria = models.ForeignKey(CategoriaServico, on_delete=models.CASCADE, related_name='servicos')
    nome = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    descricao_curta = models.CharField(max_length=300)
    descricao_completa = models.TextField()
    caracteristicas = models.JSONField(default=list, help_text="Lista de características do serviço")
    tecnologias = models.JSONField(default=list, help_text="Lista de tecnologias utilizadas")
    tempo_estimado = models.CharField(max_length=100, blank=True)
    preco_inicial = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    imagem = models.ImageField(upload_to='servicos/', blank=True, null=True)
    destaque = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['categoria__ordem', 'nome']
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.nome

class Tecnologia(models.Model):
    """Tecnologias utilizadas pela consultoria"""
    TIPO_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('mobile', 'Mobile'),
        ('devops', 'DevOps'),
        ('database', 'Banco de Dados'),
        ('cloud', 'Cloud'),
        ('ai_ml', 'IA/ML'),
        ('outros', 'Outros'),
    ]
    
    nome = models.CharField(max_length=100, unique=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    descricao = models.TextField()
    logo = models.ImageField(upload_to='tecnologias/', blank=True, null=True)
    nivel_expertise = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text="Nível de expertise de 1 a 10"
    )
    anos_experiencia = models.PositiveIntegerField(default=0)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['tipo', 'nivel_expertise', 'nome']
        verbose_name = "Tecnologia"
        verbose_name_plural = "Tecnologias"
    
    def __str__(self):
        return self.nome

class Projeto(models.Model):
    """Projetos realizados pela consultoria"""
    STATUS_CHOICES = [
        ('em_desenvolvimento', 'Em Desenvolvimento'),
        ('concluido', 'Concluído'),
        ('em_manutencao', 'Em Manutenção'),
        ('arquivado', 'Arquivado'),
    ]
    
    nome = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    cliente = models.CharField(max_length=200)
    descricao = models.TextField()
    desafios = models.TextField(blank=True)
    solucoes = models.TextField(blank=True)
    tecnologias = models.ManyToManyField(Tecnologia, related_name='projetos')
    categoria_servico = models.ForeignKey(CategoriaServico, on_delete=models.SET_NULL, null=True)
    imagem_principal = models.ImageField(upload_to='projetos/')
    imagens_adicionais = models.JSONField(default=list, help_text="Lista de URLs de imagens adicionais")
    url_projeto = models.URLField(blank=True)
    url_github = models.URLField(blank=True)
    data_inicio = models.DateField()
    data_conclusao = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='em_desenvolvimento')
    destaque = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-data_inicio']
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.nome

class MembroEquipe(models.Model):
    """Membros da equipe da consultoria"""
    CARGO_CHOICES = [
        ('ceo', 'CEO'),
        ('cto', 'CTO'),
        ('tech_lead', 'Tech Lead'),
        ('senior_dev', 'Desenvolvedor Sênior'),
        ('dev', 'Desenvolvedor'),
        ('designer', 'Designer'),
        ('devops', 'DevOps'),
        ('analista', 'Analista'),
        ('estagiario', 'Estagiário'),
    ]
    
    nome = models.CharField(max_length=200)
    cargo = models.CharField(max_length=20, choices=CARGO_CHOICES)
    bio = models.TextField()
    especialidades = models.JSONField(default=list, help_text="Lista de especialidades")
    tecnologias = models.ManyToManyField(Tecnologia, related_name='membros_equipe')
    foto = models.ImageField(upload_to='equipe/')
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    anos_experiencia = models.PositiveIntegerField(default=0)
    destaque = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)
    data_entrada = models.DateField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['cargo', 'nome']
        verbose_name = "Membro da Equipe"
        verbose_name_plural = "Membros da Equipe"
    
    def __str__(self):
        return f"{self.nome} - {self.get_cargo_display()}"

class Depoimento(models.Model):
    """Depoimentos de clientes"""
    cliente = models.CharField(max_length=200)
    cargo = models.CharField(max_length=200)
    empresa = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='depoimentos/', blank=True, null=True)
    depoimento = models.TextField()
    projeto_relacionado = models.ForeignKey(Projeto, on_delete=models.SET_NULL, null=True, blank=True)
    avaliacao = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Avaliação de 1 a 5 estrelas"
    )
    destaque = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-data_criacao']
        verbose_name = "Depoimento"
        verbose_name_plural = "Depoimentos"
    
    def __str__(self):
        return f"{self.cliente} - {self.empresa}"

class BlogPost(models.Model):
    """Posts do blog da consultoria"""
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    resumo = models.CharField(max_length=300)
    conteudo = models.TextField()
    imagem_destaque = models.ImageField(upload_to='blog/')
    autor = models.ForeignKey(MembroEquipe, on_delete=models.SET_NULL, null=True)
    tags = models.JSONField(default=list, help_text="Lista de tags")
    tecnologias_relacionadas = models.ManyToManyField(Tecnologia, blank=True)
    visualizacoes = models.PositiveIntegerField(default=0)
    tempo_leitura = models.PositiveIntegerField(help_text="Tempo de leitura em minutos")
    destaque = models.BooleanField(default=False)
    publicado = models.BooleanField(default=False)
    data_publicacao = models.DateTimeField(null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-data_publicacao', '-data_criacao']
        verbose_name = "Post do Blog"
        verbose_name_plural = "Posts do Blog"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.titulo

class Contato(models.Model):
    """Formulário de contato"""
    TIPO_CHOICES = [
        ('orcamento', 'Orçamento'),
        ('duvida', 'Dúvida'),
        ('parceria', 'Parceria'),
        ('trabalhe_conosco', 'Trabalhe Conosco'),
        ('outros', 'Outros'),
    ]
    
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=20, blank=True)
    empresa = models.CharField(max_length=200, blank=True)
    tipo_contato = models.CharField(max_length=20, choices=TIPO_CHOICES)
    assunto = models.CharField(max_length=200)
    mensagem = models.TextField()
    servico_interesse = models.ForeignKey(Servico, on_delete=models.SET_NULL, null=True, blank=True)
    orcamento_estimado = models.CharField(max_length=100, blank=True)
    lido = models.BooleanField(default=False)
    respondido = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-data_criacao']
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"
    
    def __str__(self):
        return f"{self.nome} - {self.assunto}"

class ConfiguracaoSite(models.Model):
    """Configurações gerais do site"""
    nome_empresa = models.CharField(max_length=200)
    slogan = models.CharField(max_length=300)
    descricao_empresa = models.TextField()
    logo = models.ImageField(upload_to='config/')
    favicon = models.ImageField(upload_to='config/')
    email_contato = models.EmailField()
    telefone = models.CharField(max_length=20)
    whatsapp = models.CharField(max_length=20)
    endereco = models.TextField()
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    meta_description = models.CharField(max_length=300)
    meta_keywords = models.CharField(max_length=500)
    google_analytics = models.TextField(blank=True)
    pixel_facebook = models.TextField(blank=True)
    mostrar_servicos = models.BooleanField(default=True, help_text="Exibir item Serviços no menu")
    mostrar_sobre = models.BooleanField(default=True, help_text="Exibir item Sobre no menu")
    mostrar_portfolio = models.BooleanField(default=True, help_text="Exibir item Portfólio no menu")
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Configuração do Site"
        verbose_name_plural = "Configurações do Site"
    
    def __str__(self):
        return f"Configuração - {self.nome_empresa}"

class Newsletter(models.Model):
    """Inscrições na newsletter"""
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=200, blank=True)
    ativo = models.BooleanField(default=True)
    data_inscricao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-data_inscricao']
        verbose_name = "Newsletter"
        verbose_name_plural = "Newsletters"
    
    def __str__(self):
        return self.email
