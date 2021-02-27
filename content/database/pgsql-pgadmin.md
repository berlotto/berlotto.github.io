Title: Executando queries e gerenciando o postgres de forma fácil
Date: 2021-02-27 13:00
Category: database
Tags: postgres, bancodedados, dados, pgsql
Slug: executando-queries-e-gerenciando-postgres-de-forma-facil
Authors: Sérgio Berlotto
Summary: 
    Chega de passar trabalho e ficar catando ferramentas que possibilitem
    você tanto a gerenciar seu banco quanto a consultar os dados. Vou te mostrar
    como fazer isso de forma fácil com uma ferramenta que está muito madura e
    com desenvolvimento muito ativo pela comunidade.
Headline: PgAadmin - a velha ferramenta, com nova cara
Header_Cover: static/posts/pgadmin.jpg

# Postgres PgAdmin

Vamos então começar do início: O que é o pgAdmin ?

O pgAdmin é uma ferramenta que permite administrar completamente seu banco de dados Postgres.

Com ele conseguimos controlar tudo que um DBA necessita por exemplo: conexões, usuários e permissões,
databases, tabelas, e tudo mais, mas, também, é possível gerenciar os dados de um banco de dados, que 
geralmente é um trabalho que o desenvolvedor está mais preocupado. O dev pode, por exemplo, criar as conexões para o banco local, remoto de testes e ambiente de produção se tiver permissão.

Assim o desenvolvedor consegue utilizar esta interface tanto quanto um DBA.

O pgAdmin está na sua versão 4 e atualmente é web mas já foi uma ferramenta de interface gráfica na 
sua versão 3, veja como era:

![antigo pgAdmin 3](/static/posts/pgadmin/pgadmin3.jpg)

Este formato de trabalho foi migrado para uma aplicação web, o que facilitou muitas coisas para todos,
podemos instalar apenas 1 pgadmin e gerenciar usuários e conexões centralizadamente dentro da empresa
por exemplo, podemos subir pgAdmins locais através de docker em ambiente de desenvolvimento,
podemos fazer várias coisas que com o antigo não daria. Além de estar muito mais bonito e com seu
desenvolvimento muito ativo.

## Conhecendo

Então vamos lá, vamos conhecer o atual pgAdmin 4

Esta é a tela de login:

![antigo pgAdmin 3](/static/posts/pgadmin/login.png)

E esta é a interface principal de trabalho:

![antigo pgAdmin 3](/static/posts/pgadmin/interface.png)

Dê uma olhada rapida, como fazer o login e utilizar alguns controles no pgadmin:

<iframe width="560" height="315" src="https://www.youtube.com/embed/BQKRupBi700" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Neste video eu mostro como criar um novo servidor para acessar, informar o host, usuário e senha,
como acessar a área de gestão dos componentes da instância, ao lado esquerdo, como acessar a tela
de query, e como executar um explain analyse, que é muito importante na hora queremos debugar nossa
query.

Este banco local de exemplo ai, tem somente uma tabela bem simples inventada, mas já nos permite ver
como o explain analyse mostra suas informações, muito completas e detalhadas e ainda conseguimos 
configurar o que precisamos medir, como timing, custos, buffers, entre outros.

## Como executar

Bom, como tudo hoje pode ser executado dentro de um docker, com o pgAdmin, não seria diferente.

Primeiro, lembrando que o pgAdmin 4 é opensource, e você pode dar uma espiada no código se quiser. 
Veja na documentação sobre isso: https://www.pgadmin.org/development/resources/

Bom, o docker-compose auxilia muito quanto pretendemos iniciar containers dependentes ou até quando
queremos documentar containers em execução.

E é ele que iremos utilizar. Neste docker-compose eu subo um banco PostgreSQL para que vocẽ possa 
testar os comandos todos, mas se você já tem uma instancia de Postgres no ar, nao precisa subir tudo,
daí, você pode escolher o que fazer: 

* ou você adiciona somente a parte do pgAdmin no seu docker-compose onde já tem o banco
* ou você sobre este docker-compose mesmo para subir o pgAdmin e um banco junto
* ou ainda, você pode subir somente o pgAdmin para acessar outros bancos que deseje

```yaml
version: "3.9"
services:
postgres:
    image: postgres:13-alpine
    environment:
    - POSTGRES_PASSWORD=admin123
    - POSTGRES_DB=db1
    ports:
    - "5432:5432"
pgadmin:
    image: dpage/pgadmin4
    environment:
    - PGADMIN_DEFAULT_EMAIL=admin
    - PGADMIN_DEFAULT_PASSWORD=admin123
    ports:
    - "8080:80"
```

Bom, explicando um pouco:

O serviço "postgres" é a instancia de banco, fica com o hostname "postgres" no container e isso
é um padrão docker-compose. Definimos ali também o password do usuário padrão que é também "postgres"
e um banco que irá ser criado também, chamdao "db1".

O serviço "pgadmin" é o que nos interessa. A imagem do pgadmin é "dpage/pgadmin4". Quando sai uma versão nova do pgadmin, 
no meu ambiente local, eu simplesmente removo o container e a imagem, faço pull da imagem novamente e recrio o container.

Neste serviço também definimos duas variaveis de ambiente que definem um usuário administrador e senha para ele, além de
direcionar a porta 80 de dentro do container para a porta 8080 da máquina local.

Dito isto, podemos executar:

```shell
$ docker-compose up
```

Então agora é só acessar no seu browser http://localhost:8080 e você vera aquela tela de login que mostrei mais acima.

## Explain [analyse]

Uma das ferramentas que mais tenho utilizado nos ultimos tempos é o Explain e o explain analyse no pgAdmin.

Estes dois comandos, no Postgres, explican como a query está sendo executada dentro do banco, eles mostram quais as escolhas
o banco de dados fez para executar sua consulta e por que, além de mostrar também, quando solicitado, os tempos de execução e 
todos os custos que o banco teve para retornar seu dado.

Se está conseguindo utilizar o indice esperado, quantos loops o banco fez para pegar os registros, quanto custou para o banco
retornar aqueles dados.

Estes comandos funcionam muito bem no terminal, via psql, mas quando temos estas informações de forma visual tudo fica muito
mais fácil.

Veja um exemplo do proprio site do pgAdmin:

![antigo pgAdmin 3](/static/posts/pgadmin/pgadmin4-explain.jpg)

## Conclusão

Além disso, muitas outras funções do banco de dados podem ser acessadas e gerenciadas. O pgAdmin é muito completo e muito leve.
Em um dashboard muito visual você consegue ver toda a atividade que está acontendo no seu banco de dados, em outra tela você
consegue ver todos os resources disponíveis no banco, e também codificar suas procedures, e por ai vai.

Você, desenvolvedor, não precisa mais ficar se batendo a procura de uma boa ferramenta, usa o pgAdmin

Site oficial: [https://www.pgadmin.org/](https://www.pgadmin.org/)