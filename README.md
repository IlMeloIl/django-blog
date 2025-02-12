# Blog em Django

Uma plataforma de blog completa com autenticação de usuários, CRUD de posts/comentários e painel administrativo.

## Funcionalidades

- **Autenticação de Usuários**
  - Login/Registro com validação
  - Controle de sessões
- **Gestão de Conteúdo**
  - Criação/Edição de posts com editor rico
  - Sistema de comentários
  - Status de posts (Rascunho/Publicado/Arquivado)
- **Recursos Avançados**
  - Paginação inteligente
  - Busca por conteúdo
  - URLs amigáveis (slug)
  - Design responsivo
- **Administração**
  - Painel admin customizado
  - Moderação de conteúdo

## Pré-requisitos

- Python 3.11.9
- pip
- venv (recomendado)

## Instalação

```bash
# Clonar repositório
git clone https://github.com/seu-usuario/blog-platform.git
cd blog-platform

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Instalar dependências
pip install -r requirements.txt

# Configurar ambiente
export SECRET_KEY='sua-chave-secreta'  # Adicione ao .env posteriormente
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Estrutura do Projeto
```
blog-platform/
├── apps/
│   ├── accounts/      # Autenticação
│   └── blog/          # Lógica principal
├── setup/             # Configurações Django
├── templates/         # Arquivos HTML
└── static/            # CSS/JS/Imagens
```

## Uso

- Acesse http://localhost:8000
- **Usuário Comum:**
  - Navegue pelos posts
  - Comente em publicações

- **Administrador:**
  - Acesse /admin          
  - Gerencie posts/comentários
  - Controle status de publicação

## Customização
Configurações importantes no .env:
```
SECRET_KEY='sua-chave-secreta-aqui'
```
