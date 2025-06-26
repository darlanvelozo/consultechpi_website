# ConsulTechPI - Site Institucional

Site institucional moderno para consultoria tecnológica especializada em criação de sites, sistemas e automação.

## 🚀 Características

- **Design Moderno e Responsivo**: Interface adaptável para todos os dispositivos
- **SEO Otimizado**: Meta tags, sitemap XML e estrutura semântica
- **Painel Administrativo**: Gerenciamento completo de conteúdo via Django Admin
- **Blog Integrado**: Sistema de blog com categorização e busca
- **Portfólio de Projetos**: Exibição profissional dos trabalhos realizados
- **Formulários de Contato**: Sistema de captura de leads e orçamentos
- **Newsletter**: Sistema de inscrição para marketing
- **Tecnologias**: Exibição das tecnologias dominadas pela equipe

## 🛠️ Tecnologias Utilizadas

- **Backend**: Django 5.2.3
- **Frontend**: HTML5, CSS3, JavaScript
- **Banco de Dados**: SQLite (desenvolvimento) / PostgreSQL (produção)
- **Frameworks CSS**: Bootstrap 5
- **Ícones**: Font Awesome
- **Deploy**: Docker (recomendado)

## 📋 Pré-requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)
- Git

## 🔧 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/consultechpi.git
cd consultechpi
```

### 2. Crie um ambiente virtual
```bash
python -m venv venv

# Ative o ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto:
```env
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Execute as migrações
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crie um superusuário
```bash
python manage.py createsuperuser
```

### 7. Execute o servidor de desenvolvimento
```bash
python manage.py runserver
```

O site estará disponível em: http://127.0.0.1:8000/

## 📁 Estrutura do Projeto

```
site_consultechpi/
├── site_consultechpi/          # Configurações do projeto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── web_site/                   # Aplicação principal
│   ├── models.py              # Modelos de dados
│   ├── views.py               # Lógica de visualização
│   ├── admin.py               # Configuração do admin
│   ├── forms.py               # Formulários
│   └── urls.py                # URLs da aplicação
├── templates/                 # Templates HTML
├── static/                    # Arquivos estáticos (CSS, JS, imagens)
├── media/                     # Uploads de mídia
├── requirements.txt           # Dependências Python
└── README.md                  # Este arquivo
```

## 🎯 Modelos de Dados

### Principais Entidades:

1. **CategoriaServico**: Categorias de serviços (Desenvolvimento Web, Mobile, etc.)
2. **Servico**: Serviços oferecidos com detalhes e preços
3. **Tecnologia**: Stack tecnológico da empresa
4. **Projeto**: Portfólio de projetos realizados
5. **MembroEquipe**: Equipe da consultoria
6. **Depoimento**: Testimonials de clientes
7. **BlogPost**: Posts do blog
8. **Contato**: Formulários de contato
9. **ConfiguracaoSite**: Configurações gerais do site
10. **Newsletter**: Inscrições na newsletter

## 🎨 Personalização

### 1. Configurações do Site
Acesse o admin em `/admin/` e configure:
- Nome da empresa
- Logo e favicon
- Informações de contato
- Redes sociais
- Meta tags para SEO

### 2. Conteúdo
- Adicione serviços e categorias
- Cadastre projetos do portfólio
- Crie posts para o blog
- Adicione membros da equipe
- Configure depoimentos de clientes

### 3. Design
- Edite os templates em `templates/web_site/`
- Personalize CSS em `static/css/`
- Adicione JavaScript em `static/js/`

## 📧 Configuração de Email

Para produção, configure o email no `settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'seu-email@gmail.com'
EMAIL_HOST_PASSWORD = 'sua-senha-de-app'
```

## 🚀 Deploy

### Usando Docker (Recomendado)

1. Crie um `Dockerfile`:
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN python manage.py collectstatic --noinput

EXPOSE 8000
CMD ["gunicorn", "site_consultechpi.wsgi:application", "--bind", "0.0.0.0:8000"]
```

2. Crie um `docker-compose.yml`:
```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DEBUG=False
      - SECRET_KEY=sua-chave-secreta
    volumes:
      - ./media:/app/media
      - ./staticfiles:/app/staticfiles
```

3. Execute:
```bash
docker-compose up --build
```

### Deploy Manual

1. Configure um servidor web (Nginx/Apache)
2. Use Gunicorn como servidor WSGI
3. Configure PostgreSQL como banco de dados
4. Configure arquivos estáticos e mídia

## 🔒 Segurança

- Altere a `SECRET_KEY` em produção
- Configure `DEBUG=False` em produção
- Use HTTPS em produção
- Configure `ALLOWED_HOSTS` adequadamente
- Mantenha as dependências atualizadas

## 📊 Monitoramento

- Configure Google Analytics
- Configure Facebook Pixel
- Monitore logs de erro
- Configure backup automático do banco

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 📞 Suporte

Para suporte, envie um email para: contato@consultechpi.com

---

**Desenvolvido com ❤️ pela ConsulTechPI** 