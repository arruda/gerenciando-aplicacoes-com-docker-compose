![Docker-compose](img/Compose.png "Docker-compose")
# Docker-compose, pra que serve?
Facilitar sua vida, basicamente.
Ele descreve todos seus containers em um arquivo de configuração (no formato YAML), que é muito simples de ler e de escrever.

Assim, ao inves de criar containers passando comandos longos e complicados, e correndo o risco de errar alguma coisa toda vez que for criar um determinado container, basta comandos simples do `docker-compose` e o arquivo de configuração (`docker-compose.yml`) vai ser sempre usado para criar seus containers.

# Criando um docker-compose.yml
Caso a gente queira um PostgreSQL 9.3 rodando num container, com a porta 5432 sendo mapeada para a porta local 6789, com usuario e senha do postgres como `usuario` e `senha` respectivamente, basta criar um arquivo com o nome de `docker-compose.yml` com o seguinte conteudo:

```yaml

db:
  image: postgres:9.3
  environment:
    - POSTGRES_USER=usuario
    - POSTGRES_PASSWORD=senha
  ports:
    - "6789:5432"
```

# Contralando um container usando docker-compose
Agora que temos nosso arquivo de configuração, podemos criar e controlar esse container usando uma série de comandos do `docker-compose`


## UP
É a primeira coisa que você vai fazer, isso vai criar os containers definidos no `docker-compose.yml`, e ficara com o terminal preso no log dos mesmos.

Exemplo:
`$ docker-compose up`
ou podemos ser ainda mais especificos, caso existam muitos containers definidos no arquivo e não precisemos deles todos ligados:

`$ docker-compose up db` ou `$ docker-compose up algumservico`

Outra coisa muito comum, é usar o `-d` depois do comando `up`, para faze-lo rodar em `background`.

Exemplo:
`$ docker-compose up -d db`

## PS
Acabamos de levantar (`up`) o container pela primeira vez, mas como sabemos se ela ainda esta rodando, se por alguma razão inesperada ele acabou fechando, ou então, quais portas estão mapeadas no mesmo?

Basta usar o `$ docker-compose ps`

Ele vai listar:
 * o nome do container (containers são nomeados como `<nome_da_pasta>_<nomedocontainer>_x`, ex: `meu_projeto_db_1`)
 * o comando que está/estava rodando no container
 * Status (ligado, desligado, qual saida, etc..)
 * Portas mapeadas

## STOP
Para fazer com que os containers parem, basta executar o comando:
`$ docker-compose stop`
Ou caso queira parar apenas algum container e não todos: `$ docker-compose stop nomedocontainer`

## START
Uma vez que um container tenha sido parado, você pode religa-lo, isso é, fazer com que aquele container execute o mesmo comando outra vez, a partir estado que ele tinha parado antes.

Exemplo:
`$ docker-compose start db`

### Diferença entre UP e START
`Up` levanta uma nova instancia (container), usando como base a imagem definida para o mesmo, ou recria um container existente (deleta e criar um novo).
`Start` apenas inicia um container que estava parado anteriormente, não serve para criar um container.

Portanto, a ideia geral é: `up` você usa na primeira vez, pra criar um container, e `start` usa nas outras vezes para ligar esse mesmo container.

## RM

Para remover um container (que esteja parado), basta rodar: `$ docker-compose rm nomedocontainer`


[Exemplo de Aplicação](exemplo_app.md)