from django.core.management.base import BaseCommand
from django.utils import timezone
from web_site.models import (
    CategoriaServico, Servico, Tecnologia, Projeto, MembroEquipe,
    Depoimento, BlogPost, ConfiguracaoSite
)

class Command(BaseCommand):
    help = 'Popula o banco de dados com dados de exemplo para a ConsulTechPI'

    def handle(self, *args, **options):
        self.stdout.write('🚀 Iniciando população do banco de dados...')
        
        # Criar configuração do site
        self.create_site_config()
        
        # Criar categorias de serviços
        self.create_service_categories()
        
        # Criar tecnologias
        self.create_technologies()
        
        # Criar serviços
        self.create_services()
        
        # Criar equipe
        self.create_team()
        
        # Criar projetos
        self.create_projects()
        
        # Criar depoimentos
        self.create_testimonials()
        
        # Criar posts do blog
        self.create_blog_posts()
        
        self.stdout.write(self.style.SUCCESS('✅ Banco de dados populado com sucesso!'))

    def create_site_config(self):
        """Cria configuração inicial do site"""
        if not ConfiguracaoSite.objects.exists():
            ConfiguracaoSite.objects.create(
                nome_empresa="ConsulTechPI",
                slogan="Transformando ideias em soluções tecnológicas inovadoras",
                descricao_empresa="Somos uma consultoria tecnológica especializada em desenvolvimento de sites, sistemas e automação. Nossa missão é transformar ideias em soluções digitais que impulsionam o crescimento dos nossos clientes.",
                email_contato="contato@consultechpi.com",
                telefone="(11) 99999-9999",
                whatsapp="(11) 99999-9999",
                endereco="São Paulo, SP - Brasil",
                linkedin="https://linkedin.com/company/consultechpi",
                github="https://github.com/consultechpi",
                instagram="https://instagram.com/consultechpi",
                youtube="https://youtube.com/@consultechpi",
                meta_description="ConsulTechPI - Consultoria tecnológica especializada em desenvolvimento de sites, sistemas e automação. Transformamos ideias em soluções digitais inovadoras.",
                meta_keywords="consultoria tecnológica, desenvolvimento web, sistemas, automação, sites, aplicativos, tecnologia"
            )
            self.stdout.write('✅ Configuração do site criada')

    def create_service_categories(self):
        """Cria categorias de serviços"""
        categories_data = [
            {
                'nome': 'Desenvolvimento Web',
                'descricao': 'Sites e aplicações web modernas e responsivas',
                'icone': 'fas fa-globe',
                'ordem': 1
            },
            {
                'nome': 'Desenvolvimento Mobile',
                'descricao': 'Aplicativos nativos e híbridos para iOS e Android',
                'icone': 'fas fa-mobile-alt',
                'ordem': 2
            },
            {
                'nome': 'Sistemas Empresariais',
                'descricao': 'Sistemas personalizados para otimizar processos',
                'icone': 'fas fa-building',
                'ordem': 3
            },
            {
                'nome': 'Automação',
                'descricao': 'Automação de processos e workflows',
                'icone': 'fas fa-robot',
                'ordem': 4
            },
            {
                'nome': 'Consultoria',
                'descricao': 'Consultoria estratégica em tecnologia',
                'icone': 'fas fa-chart-line',
                'ordem': 5
            }
        ]
        
        for data in categories_data:
            CategoriaServico.objects.get_or_create(
                nome=data['nome'],
                defaults=data
            )
        self.stdout.write('✅ Categorias de serviços criadas')

    def create_technologies(self):
        """Cria tecnologias"""
        technologies_data = [
            # Frontend
            {'nome': 'React', 'tipo': 'frontend', 'descricao': 'Biblioteca JavaScript para interfaces', 'nivel_expertise': 9, 'anos_experiencia': 4},
            {'nome': 'Vue.js', 'tipo': 'frontend', 'descricao': 'Framework progressivo para interfaces', 'nivel_expertise': 8, 'anos_experiencia': 3},
            {'nome': 'Angular', 'tipo': 'frontend', 'descricao': 'Framework completo para aplicações web', 'nivel_expertise': 7, 'anos_experiencia': 3},
            {'nome': 'Bootstrap', 'tipo': 'frontend', 'descricao': 'Framework CSS para design responsivo', 'nivel_expertise': 9, 'anos_experiencia': 5},
            
            # Backend
            {'nome': 'Django', 'tipo': 'backend', 'descricao': 'Framework Python para desenvolvimento web', 'nivel_expertise': 9, 'anos_experiencia': 5},
            {'nome': 'Node.js', 'tipo': 'backend', 'descricao': 'Runtime JavaScript para servidor', 'nivel_expertise': 8, 'anos_experiencia': 4},
            {'nome': 'Python', 'tipo': 'backend', 'descricao': 'Linguagem de programação versátil', 'nivel_expertise': 9, 'anos_experiencia': 6},
            {'nome': 'PHP', 'tipo': 'backend', 'descricao': 'Linguagem para desenvolvimento web', 'nivel_expertise': 7, 'anos_experiencia': 4},
            
            # Mobile
            {'nome': 'React Native', 'tipo': 'mobile', 'descricao': 'Framework para apps nativos', 'nivel_expertise': 8, 'anos_experiencia': 3},
            {'nome': 'Flutter', 'tipo': 'mobile', 'descricao': 'Framework Google para apps multiplataforma', 'nivel_expertise': 7, 'anos_experiencia': 2},
            
            # Database
            {'nome': 'PostgreSQL', 'tipo': 'database', 'descricao': 'Banco de dados relacional avançado', 'nivel_expertise': 8, 'anos_experiencia': 4},
            {'nome': 'MySQL', 'tipo': 'database', 'descricao': 'Sistema de gerenciamento de banco de dados', 'nivel_expertise': 7, 'anos_experiencia': 4},
            {'nome': 'MongoDB', 'tipo': 'database', 'descricao': 'Banco de dados NoSQL', 'nivel_expertise': 6, 'anos_experiencia': 2},
            
            # Cloud
            {'nome': 'AWS', 'tipo': 'cloud', 'descricao': 'Serviços em nuvem da Amazon', 'nivel_expertise': 7, 'anos_experiencia': 3},
            {'nome': 'Google Cloud', 'tipo': 'cloud', 'descricao': 'Plataforma de computação em nuvem', 'nivel_expertise': 6, 'anos_experiencia': 2},
            
            # DevOps
            {'nome': 'Docker', 'tipo': 'devops', 'descricao': 'Containerização de aplicações', 'nivel_expertise': 8, 'anos_experiencia': 3},
            {'nome': 'Git', 'tipo': 'devops', 'descricao': 'Controle de versão distribuído', 'nivel_expertise': 9, 'anos_experiencia': 5},
        ]
        
        for data in technologies_data:
            Tecnologia.objects.get_or_create(
                nome=data['nome'],
                defaults=data
            )
        self.stdout.write('✅ Tecnologias criadas')

    def create_services(self):
        """Cria serviços"""
        web_cat = CategoriaServico.objects.get(nome='Desenvolvimento Web')
        mobile_cat = CategoriaServico.objects.get(nome='Desenvolvimento Mobile')
        sistemas_cat = CategoriaServico.objects.get(nome='Sistemas Empresariais')
        
        services_data = [
            {
                'categoria': web_cat,
                'nome': 'Site Institucional',
                'descricao_curta': 'Sites profissionais para empresas',
                'descricao_completa': 'Desenvolvimento de sites institucionais modernos, responsivos e otimizados para SEO. Inclui design personalizado, integração com redes sociais e painel administrativo.',
                'caracteristicas': ['Design responsivo', 'SEO otimizado', 'Painel admin', 'Integração social'],
                'tecnologias': ['React', 'Django', 'Bootstrap'],
                'tempo_estimado': '2-4 semanas',
                'preco_inicial': 5000.00,
                'destaque': True
            },
            {
                'categoria': web_cat,
                'nome': 'E-commerce',
                'descricao_curta': 'Lojas virtuais completas',
                'descricao_completa': 'Desenvolvimento de lojas virtuais com sistema de pagamento, gestão de produtos, controle de estoque e relatórios de vendas.',
                'caracteristicas': ['Sistema de pagamento', 'Gestão de produtos', 'Controle de estoque', 'Relatórios'],
                'tecnologias': ['Vue.js', 'Django', 'PostgreSQL'],
                'tempo_estimado': '6-8 semanas',
                'preco_inicial': 15000.00,
                'destaque': True
            },
            {
                'categoria': mobile_cat,
                'nome': 'App Mobile',
                'descricao_curta': 'Aplicativos para iOS e Android',
                'descricao_completa': 'Desenvolvimento de aplicativos móveis nativos e híbridos com interface intuitiva e funcionalidades avançadas.',
                'caracteristicas': ['Multiplataforma', 'Interface intuitiva', 'Push notifications', 'Offline mode'],
                'tecnologias': ['React Native', 'Node.js'],
                'tempo_estimado': '8-12 semanas',
                'preco_inicial': 25000.00,
                'destaque': True
            },
            {
                'categoria': sistemas_cat,
                'nome': 'Sistema ERP',
                'descricao_curta': 'Sistemas de gestão empresarial',
                'descricao_completa': 'Desenvolvimento de sistemas ERP personalizados para otimizar processos internos da empresa.',
                'caracteristicas': ['Gestão financeira', 'Controle de estoque', 'RH', 'Relatórios'],
                'tecnologias': ['Django', 'PostgreSQL', 'React'],
                'tempo_estimado': '12-16 semanas',
                'preco_inicial': 50000.00,
                'destaque': False
            }
        ]
        
        for data in services_data:
            Servico.objects.get_or_create(
                nome=data['nome'],
                defaults=data
            )
        self.stdout.write('✅ Serviços criados')

    def create_team(self):
        """Cria membros da equipe"""
        team_data = [
            {
                'nome': 'João Silva',
                'cargo': 'ceo',
                'bio': 'Fundador e CEO da ConsulTechPI. Especialista em estratégia de negócios e inovação tecnológica.',
                'especialidades': ['Estratégia de negócios', 'Inovação', 'Gestão de projetos'],
                'anos_experiencia': 10,
                'destaque': True
            },
            {
                'nome': 'Maria Santos',
                'cargo': 'cto',
                'bio': 'CTO com vasta experiência em arquitetura de software e liderança técnica.',
                'especialidades': ['Arquitetura de software', 'DevOps', 'Cloud Computing'],
                'anos_experiencia': 8,
                'destaque': True
            },
            {
                'nome': 'Pedro Costa',
                'cargo': 'tech_lead',
                'bio': 'Tech Lead especializado em desenvolvimento full-stack e metodologias ágeis.',
                'especialidades': ['Full-stack development', 'Metodologias ágeis', 'Code review'],
                'anos_experiencia': 6,
                'destaque': True
            },
            {
                'nome': 'Ana Oliveira',
                'cargo': 'senior_dev',
                'bio': 'Desenvolvedora sênior com foco em frontend e experiência do usuário.',
                'especialidades': ['Frontend development', 'UX/UI', 'React'],
                'anos_experiencia': 5,
                'destaque': False
            }
        ]
        
        for data in team_data:
            member, created = MembroEquipe.objects.get_or_create(
                nome=data['nome'],
                defaults={
                    **data,
                    'data_entrada': timezone.now().date()
                }
            )
            if created:
                # Adicionar tecnologias relacionadas
                if data['cargo'] in ['cto', 'tech_lead']:
                    techs = Tecnologia.objects.filter(nivel_expertise__gte=7)[:5]
                    member.tecnologias.set(techs)
                elif data['cargo'] == 'senior_dev':
                    techs = Tecnologia.objects.filter(tipo='frontend')[:3]
                    member.tecnologias.set(techs)
        
        self.stdout.write('✅ Equipe criada')

    def create_projects(self):
        """Cria projetos de exemplo"""
        web_cat = CategoriaServico.objects.get(nome='Desenvolvimento Web')
        
        projects_data = [
            {
                'nome': 'E-commerce Fashion',
                'cliente': 'Moda Express',
                'descricao': 'Desenvolvimento de loja virtual completa para empresa de moda',
                'desafios': 'Integração com múltiplos gateways de pagamento e sistema de gestão de estoque complexo',
                'solucoes': 'Implementação de arquitetura modular com APIs REST e sistema de cache inteligente',
                'categoria_servico': web_cat,
                'data_inicio': timezone.now().date(),
                'status': 'concluido',
                'destaque': True
            },
            {
                'nome': 'App de Delivery',
                'cliente': 'FastFood Delivery',
                'descricao': 'Aplicativo mobile para delivery de comida',
                'desafios': 'Sistema de geolocalização em tempo real e integração com múltiplos restaurantes',
                'solucoes': 'Uso de React Native com APIs de geolocalização e sistema de notificações push',
                'categoria_servico': web_cat,
                'data_inicio': timezone.now().date(),
                'status': 'em_desenvolvimento',
                'destaque': True
            }
        ]
        
        for data in projects_data:
            project, created = Projeto.objects.get_or_create(
                nome=data['nome'],
                defaults=data
            )
            if created:
                # Adicionar tecnologias relacionadas
                techs = Tecnologia.objects.filter(ativo=True)[:4]
                project.tecnologias.set(techs)
        
        self.stdout.write('✅ Projetos criados')

    def create_testimonials(self):
        """Cria depoimentos de clientes"""
        testimonials_data = [
            {
                'cliente': 'Carlos Mendes',
                'cargo': 'Diretor de Marketing',
                'empresa': 'Moda Express',
                'depoimento': 'A ConsulTechPI transformou nossa presença digital. O e-commerce superou todas as expectativas e as vendas aumentaram 300% no primeiro mês.',
                'avaliacao': 5,
                'destaque': True
            },
            {
                'cliente': 'Fernanda Lima',
                'cargo': 'CEO',
                'empresa': 'FastFood Delivery',
                'depoimento': 'Profissionalismo e qualidade técnica excepcionais. O app desenvolvido pela equipe é um sucesso entre nossos clientes.',
                'avaliacao': 5,
                'destaque': True
            }
        ]
        
        for data in testimonials_data:
            Depoimento.objects.get_or_create(
                cliente=data['cliente'],
                empresa=data['empresa'],
                defaults=data
            )
        
        self.stdout.write('✅ Depoimentos criados')

    def create_blog_posts(self):
        """Cria posts do blog"""
        posts_data = [
            {
                'titulo': 'Tendências em Desenvolvimento Web para 2024',
                'resumo': 'Descubra as principais tecnologias e metodologias que estão moldando o desenvolvimento web este ano.',
                'conteudo': 'O desenvolvimento web está em constante evolução...',
                'tags': ['desenvolvimento web', 'tendências', 'tecnologia'],
                'tempo_leitura': 5,
                'destaque': True,
                'publicado': True
            },
            {
                'titulo': 'Como escolher a melhor tecnologia para seu projeto',
                'resumo': 'Guia completo para escolher a stack tecnológica ideal para seu projeto.',
                'conteudo': 'A escolha da tecnologia certa é fundamental para o sucesso do projeto...',
                'tags': ['tecnologia', 'desenvolvimento', 'dicas'],
                'tempo_leitura': 8,
                'destaque': False,
                'publicado': True
            }
        ]
        
        for data in posts_data:
            BlogPost.objects.get_or_create(
                titulo=data['titulo'],
                defaults={
                    **data,
                    'data_publicacao': timezone.now()
                }
            )
        
        self.stdout.write('✅ Posts do blog criados') 