# Base Django Project

Este é um projeto base para iniciar outros projetos baseados no framework Django. Ele inclui configurações iniciais, estrutura de diretórios e um conjunto de funcionalidades comuns.


## Features

* Autenticação com [django-allauth](https://github.com/pennersr/django-allauth)
    * Email como username
    * Pronto para autenticação com serviços (github, google)
- [Bootstrap 5.3.2](https://getbootstrap.com/)
- [Toastr](https://github.com/CodeSeven/toastr) para as messages do Django
- Docker
- Docker compose
- Deploy com NGINX


## Run Locally

Clone o projeto

```bash
  git clone https://github.com/cesarfreire/base-django.git
```

Vá para o diretório

```bash
  cd base-django
```
Renomeie o arquivo `.env sample` para `.env_dev` e altere as informações.

Inicie com o docker compose

```bash
  docker compose -f docker-compose.yml up --build
```

Acesse a URL

```bash
  http://127.0.0.1:8000/accounts/login
```
