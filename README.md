# Blog em Django

Uma plataforma de blog completa com autenticação de usuários, CRUD de posts/comentários e painel administrativo.
Este projeto foi desenvolvido como parte de um processo de aprendizado em Django e desenvolvimento web. Ele não será colocado em produção ou feito deploy em um ambiente real, servindo exclusivamente para fins educacionais.

## Funcionalidades

- **Autenticação de Usuários**
  - Login/Registro com validação
  - Controle de sessões
- **Gestão de Conteúdo**
  - Criação/Edição de posts
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
https://github.com/IlMeloIl/django-blog.git
cd django-blog

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
```bash
blog-platform/
├── apps/
│   ├── accounts/      # Autenticação
│   └── blog/          # Lógica principal
├── setup/             # Configurações Django
├── templates/         # Arquivos HTML
└── static/            # CSS/JS/Imagens
```

## Gerando uma SECRET_KEY

Para rodar o projeto localmente, você precisará de uma `SECRET_KEY`. Siga os passos abaixo para gerar uma:

1. Abra um terminal Python:
```python
#Execute o seguinte código
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

2. Copie a chave gerada e adicione ao arquivo .env ou diretamente no settings.py
```
SECRET_KEY = 'sua-chave-secreta-aqui'
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
