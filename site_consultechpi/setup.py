#!/usr/bin/env python3
"""
Script de setup para o projeto ConsulTechPI
"""

import os
import sys
import subprocess
from pathlib import Path

def run_command(command, description):
    """Executa um comando e mostra o resultado"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} concluído com sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao {description.lower()}: {e}")
        print(f"Erro: {e.stderr}")
        return False

def check_python_version():
    """Verifica se a versão do Python é compatível"""
    print("🐍 Verificando versão do Python...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8+ é necessário!")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} - OK!")
    return True

def create_env_file():
    """Cria arquivo .env se não existir"""
    env_file = Path('.env')
    if not env_file.exists():
        print("📝 Criando arquivo .env...")
        env_content = """# Configurações do Django
SECRET_KEY=django-insecure-change-this-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Configurações de Email (desenvolvimento)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
"""
        with open(env_file, 'w') as f:
            f.write(env_content)
        print("✅ Arquivo .env criado!")
    else:
        print("✅ Arquivo .env já existe!")

def main():
    """Função principal do setup"""
    print("🚀 Iniciando setup do ConsulTechPI...")
    
    # Verificar Python
    if not check_python_version():
        sys.exit(1)
    
    # Criar ambiente virtual se não existir
    venv_path = Path('venv')
    if not venv_path.exists():
        print("\n📦 Criando ambiente virtual...")
        if not run_command("python -m venv venv", "Criando ambiente virtual"):
            sys.exit(1)
        print("✅ Ambiente virtual criado!")
        print("⚠️  IMPORTANTE: Ative o ambiente virtual antes de continuar:")
        print("   Windows: venv\\Scripts\\activate")
        print("   Linux/Mac: source venv/bin/activate")
        return
    else:
        print("✅ Ambiente virtual já existe!")
    
    # Criar arquivo .env
    create_env_file()
    
    # Instalar dependências
    if not run_command("pip install -r requirements.txt", "Instalando dependências"):
        sys.exit(1)
    
    # Executar migrações
    if not run_command("python manage.py makemigrations", "Criando migrações"):
        sys.exit(1)
    
    if not run_command("python manage.py migrate", "Aplicando migrações"):
        sys.exit(1)
    
    # Criar diretórios necessários
    directories = ['static', 'media', 'templates']
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
    
    print("\n🎉 Setup concluído com sucesso!")
    print("\n📋 Próximos passos:")
    print("1. Crie um superusuário: python manage.py createsuperuser")
    print("2. Inicie o servidor: python manage.py runserver")
    print("3. Acesse: http://127.0.0.1:8000/")
    print("4. Admin: http://127.0.0.1:8000/admin/")

if __name__ == "__main__":
    main() 