# Egressus

A Egressus é uma plataforma digital inovadora projetada para armazenar e acessar todas as memórias de formatura, seja em um computador ou dispositivo móvel. Eliminando a necessidade de murais físicos, a Egressus oferece uma solução moderna e eficiente para relembrar momentos especiais, manter a conexão com colegas de turma e receber notificações sobre eventos e oportunidades profissionais. A plataforma facilita a gestão e preservação de conquistas acadêmicas, proporcionando uma experiência enriquecedora e acessível para todos os usuários. 

## Tecnologias atualmente utilizadas

- DOCKER
- POSTGRESQL
- DJANGO
- SHELL SCRIPT
- GIT

## Guia rápido para desenvolvimento

### Pré-requisitos

- Docker
- Git
- VSCode
- Navegador web

### Subindo o ambiente de desenvolvimento:

#### Inserindo variáveis de ambiente

Para subir o ambiente de desenvolvimento você precisará do acesso às variáveis de ambiente, contate um desenvolvedor para liberar o acesso através do [link](https://colab.research.google.com/drive/1XL511ufZxyoWsZZOb_5LEFBQYNKCmP5T?usp=sharing).

Após o acesso, renomeie o arquivo .env-example(na pasta dotenv_files) para .env e altere os campos "change-me" presentes para os seus respectivos.

#### Subindo os containers
Abra um terminal e execute no diretório raíz do projeto:

```bash
docker compose up --build
```

Este comando criará os containeres necessários para a aplicação, caso queira que a aplicação rode em segundo plano acrescente o sufixo -d após o comando anterior.

Após subir os containers você poderá acessar a página principal do app: <http://127.0.0.1:8000>

#### Criando superusuário

Use o comando abaixo para [criar um superusuário](https://docs.djangoproject.com/pt-br/4.2/intro/tutorial02/#creating-an-admin-user) e ter acesso ao painel administrador:

```bash
docker-compose exec djangoapp python manage.py createsuperuser
```

Agora, com o usuário criado, você poderá acessar o painel de administrador: <http://127.0.0.1:8000/admin/>


#### PgAdmin

Você pode acessar o banco de dados diretamente pelo container do pgadmin: <http://localhost:5050/>

As credenciais podem ser configuradas no arquivo `docker-compose.yml`.

