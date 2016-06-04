# Exemplo de Aplicação
Vamos criar um simples aplicação web usando Flask (um microframework web em Python), e usando como banco de dados um
PostgreSQL.

## Dockerfile de uma app flask
Segue o conteúdo minimo necessário para rodar nossa aplicação web:

```
FROM ubuntu:14.04

RUN apt-get update

# python
RUN apt-get install -y python python-dev python-distribute python-pip build-essential

#Postgres deps
RUN apt-get install -y libpq-dev

# deps do nosso projeto web em python
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

VOLUME /data
```

## O que é um Volume

Quando definimos um volume num container, estamos definindo um tipo especial de diretorio.

Volumes tem várias funcionalidades, como:
 * persistir dados mesmo que o container seja deletado.
 * compartilhar uma pasta entre o Host e o container
 * compartilhar dados entre containers

Nesse exemplo de aplicação web, vamos mapear para que a pasta com o codigo fonte da aplicação web, fique na pasta `/data` dentro do container.
Com isso, toda alteração feita no codigo fonte, estará replicada dentro do container.

Fazemos isso, usando a configuração `volumes` no `docker-compose.yml`.

## Linkando containers
Permite que um container acesse as portas expostas por outro container em que ele se ligará.

Nesse exemplo de aplicação, queremos nosso container que vai rodar a aplicação web, possa acessar as portas do container do BD, portanto ligamos o container `web` ao `db` usando a configuração `links`:

```yaml
web:
  build: .
  working_dir: /data
  command: python app.py
  links:
    - db
  volumes:
    - .:/data
  ports:
    - "8080:80"

db:
  image: postgres:9.3
  environment:
    - POSTGRES_USER=sis_web
    - POSTGRES_PASSWORD=123
  ports:
    - "5432:5432"
```

## Rodando tudo
Vamos agora rodar nossos containers para que possamos ter nossa aplicação web rodando junto com o nosso banco de dados.

`$ docker-compose up -d` vai criar e iniciar os containers.


E se rodarmos o `$ docker-compose ps` teremos a seguinte saída:
```
      Name                    Command               State           Ports
----------------------------------------------------------------------------------
exemploapp_db_1    /docker-entrypoint.sh postgres   Up      0.0.0.0:5432->5432/tcp
exemploapp_web_1   python app.py                    Up      0.0.0.0:8080->80/tcp
```

se entrarmos em [localhost:8080](http://localhost:8080) acessaremos o hello world do nosso app web.

Podemos também acessar o postgres localmente na porta `5432` para ver o que tem nele.

# Como eles se comunicam?
No arquivo [app.py](exemplo_app/app.py) podemos ver na função `get_db_config` como o container de app se comunica com o container `db`.

## Rodando um comando unico

Podemos rodar um comando unico, como um script por exemplo num container definido no docker-compose.yml.

Nesse caso iremos rodar o script `prepare_db.sh` num container `web`.

Esse script faz com que a aplicação rode um comando, onde é criado um banco de dados com as tabelas usadas pela aplicação web.

Para isso faremos:

```bash
$ docker-compose run web /data/prepare_db.sh
```

Se verificarmos novamente o banco de dados, veremos que foi criado a tabela `pessoas` (relativo ao que foi definido em [models.py](exemplo_app/models.py) na aplicação web), e outras tabelas relativas a aplicação web.