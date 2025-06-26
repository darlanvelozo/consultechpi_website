# 🚀 Instruções Rápidas - ConsulTechPI

## ⚡ Setup Rápido (5 minutos)

### 1. Instalar Python e dependências
```bash
# Verificar se Python está instalado
python --version

# Se não estiver instalado, baixe em: https://python.org
```

### 2. Criar ambiente virtual
```bash
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar banco de dados
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Criar superusuário
```bash
python manage.py createsuperuser
```

### 6. Popular com dados de exemplo (opcional)
```bash
python manage.py populate_data
```

### 7. Iniciar servidor
```bash
python manage.py runserver
```

## 🌐 Acessos

- **Site**: http://127.0.0.1:8000/
- **Admin**: http://127.0.0.1:8000/admin/

## 📋 Próximos Passos

### 1. Configurar o Site
1. Acesse o admin: http://127.0.0.1:8000/admin/
2. Vá em "Configurações do Site"
3. Configure:
   - Nome da empresa
   - Logo e favicon
   - Informações de contato
   - Redes sociais

### 2. Adicionar Conteúdo
1. **Serviços**: Adicione suas categorias e serviços
2. **Equipe**: Cadastre os membros da equipe
3. **Projetos**: Adicione projetos do portfólio
4. **Blog**: Crie posts para o blog
5. **Depoimentos**: Adicione testimonials de clientes

### 3. Personalizar Design
- Edite templates em `templates/web_site/`
- Personalize CSS em `static/css/`
- Adicione JavaScript em `static/js/`

## 🎯 Estrutura Criada

### Modelos Principais:
- ✅ **CategoriaServico**: Organiza serviços por categoria
- ✅ **Servico**: Detalhes dos serviços oferecidos
- ✅ **Tecnologia**: Stack tecnológico da empresa
- ✅ **Projeto**: Portfólio de projetos
- ✅ **MembroEquipe**: Equipe da consultoria
- ✅ **Depoimento**: Testimonials de clientes
- ✅ **BlogPost**: Sistema de blog
- ✅ **Contato**: Formulários de contato
- ✅ **ConfiguracaoSite**: Configurações gerais
- ✅ **Newsletter**: Sistema de captura de leads

### Funcionalidades:
- ✅ Painel admin profissional
- ✅ SEO otimizado
- ✅ Sistema de blog
- ✅ Portfólio dinâmico
- ✅ Formulários inteligentes
- ✅ Newsletter
- ✅ Responsivo e moderno

## 🔧 Comandos Úteis

```bash
# Criar migrações após alterar modelos
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Popular com dados de exemplo
python manage.py populate_data

# Coletar arquivos estáticos
python manage.py collectstatic

# Shell do Django
python manage.py shell

# Verificar problemas
python manage.py check
```

## 📁 Estrutura de Arquivos

```
site_consultechpi/
├── web_site/                    # Aplicação principal
│   ├── models.py               # Modelos de dados
│   ├── views.py                # Lógica de visualização
│   ├── admin.py                # Configuração do admin
│   ├── forms.py                # Formulários
│   ├── urls.py                 # URLs da aplicação
│   └── management/             # Comandos personalizados
├── templates/                  # Templates HTML
├── static/                     # Arquivos estáticos
├── media/                      # Uploads de mídia
├── requirements.txt            # Dependências
└── README.md                   # Documentação completa
```

## 🚨 Solução de Problemas

### Erro: "pip not found"
```bash
# Instalar pip
python -m ensurepip --upgrade
```

### Erro: "Django not found"
```bash
# Verificar se ambiente virtual está ativo
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

# Reinstalar dependências
pip install -r requirements.txt
```

### Erro: "Database locked"
```bash
# Parar servidor (Ctrl+C)
# Deletar db.sqlite3
# Executar migrações novamente
python manage.py migrate
```

## 📞 Suporte

- 📧 Email: contato@consultechpi.com
- 📖 Documentação: README.md
- 🐛 Issues: GitHub Issues

---

**🎉 Seu site está pronto para demonstrar a expertise da sua consultoria!** 