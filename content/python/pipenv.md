Title: Pipenv - ambientes virtuais profissionais
Date: 2021-02-16 13:00
Category: python
Tags: python, pipenv, virtualenv
Slug: pipenv-ambientes-virtuais-profissionais
Authors: Sérgio Berlotto
Summary: Como conseguimos controlar nosso ambiente de desenvolvimento de forma profissional com o Pipenv.
Headline: O poder dos ambientes virtuais
Header_Cover: static/posts/environmental.jpg

Quem trabalha com Python sabe o quanto temos disponíveis diferentes tipos e versões de bibliotecas. 
E os ambientes virtuais vieram para nos ajudar a trabalhar com várias delas ao mesmo tempo. Mas, com eles
vieram também alguns trampos a mais ... hehe

Enntão vamos aprender a utilizar uma ferramenta que gerencia tudo pra nós!

# Pipenv

O pipenv é uma ferramenta que cria uma camada auxiliar no trabalho com os ambientes virtuais.

Vocês lembram o que são os ambientes virtuais ? 

> "Ambientes virtuais são um conjunto de diretórios que isolam versões de bibliotecas
> do Python de forma local, separando-as das versões globais que acompanham o sistema 
> operacional." 
> 
> -- <cite>[Lucas Ferreira](https://medium.com/@lucasferreiraos/python-django-e-ambientes-virtuais-uma-rela%C3%A7%C3%A3o-de-organiza%C3%A7%C3%A3o-e-produtividade-dafb51f11b23)</cite>

A ferramenta original do python criada para criar os ambientes virtuais é o `virtualenv`. Mas ele tem 
seus problemas: ele é muuuito manual, e cria o ambiente virtual no diretório corrente ou temos que 
ficar especificando os caminhos.

Daí entrou o virtualenv-wrapper, mas tem também seus poréns, com ele precisamos lembrar dos nomes
dos ambientes além de ficar ativando e desativando manual...

Além disto, em ambas é chato ficar gerenciando o famoso arquivo requirements.txt que todo pythonista
conhece. Adicionar e remover bibliotecas é um trabalho muito manual e ainda, quando necessitamos gerenciar
umas bibliotecas para ambiente de dev e outras para ambiente de produção, aí sim o negócio fica complicado.

Esses "problemas" todo dev python passa no início.. não adianta. Mas é um aprendizado, eu sempre falo que:
*antes de usar uma ferramenta de mais alto nível, aprenda o que está sendo feito por baixo dos panos*.

Em todas essas tarefas e talvez mais um pouco também o Pipenv nos auxilia muito

### Hands-on

Então vamos pôr a mão na massa.

Primeiro a instalação

    $ pip install pipenv

Agora temos que entender uma coisa que é diferente no pipenv com relação aos outros: ele
controla seu ambiente através de dois arquivos: Pipfile e Pipfile.lock

O Pipfile é atualizado cada vez que você adiciona, remove ou atualiza a versao de uma
biblioteca e juntamente com o Pipfile.lock ele gerencia de forma inteligente as 
dependencias e as bibliotecas utilizadas. 
Você não necessita alterar estes arquivos, quem faz isso é o pipenv mesmo.

### Criar o ambiente

Com o pipenv você não precisa se preocupar em utilizar o pip e o virtualenv em separados. É muito fácil iniciar um novo ambiente virtual:

Utiliza a versão 3 do interpretador do Python 

    $ pipenv --three

Utiliza a versão 2 do Python

    $ pipenv --two

Utiliza o interpretador do Python informado

    $ pipenv --python /path/to/specific/python

Além de criar o ambiente com a versão 3 do Python já instala a biblioteca pandas também

    $ pipenv install pandas --three

O nome do ambiente virtual é criado utilizando o nome da pasta onde você está, mais uma hash string, ficando algo
assim: "testepy--lF-Jmev"

Veja um exemplo:

<script id="asciicast-OnZAACzbbi4m8f5E5rRAacTW1" src="https://asciinema.org/a/OnZAACzbbi4m8f5E5rRAacTW1.js" async></script>

### Removendo

Para remover um ambiente virtual criado, basta executar `pipenv --rm` no diretório do projeto.

<script id="asciicast-4aigyui8MxLmjc4DM07h71iak" src="https://asciinema.org/a/4aigyui8MxLmjc4DM07h71iak.js" async></script>

### Gerenciando bibliotecas

Para gerenciar (instalar, atualizar e remover) bibliotecas no ambiente virtual e para que elas fiquem registradas 
corretamente no Pipfile, devemos utilizar os comandos a seguir:

Caso queira adicionar uma lib:

    $ pipenv install <lib>

Caso queira instalar todas libs definidas no Pipenv file, quando faz o clone do projeto por exemplo:

    $ pipenv install 

Caso queira remover uma lib 

    $ pipenv uninstall <lib>

Caso queira instalar de um arquivo requirements

    $ pipenv install -r requirements.txt

Caso queira atualizar as bibliotecas:

    $ pipenv update --outdated

Caso queira instalar uma lib somente para os ambiente de desenvolvimento

    $ pipenv install <lib> --dev

<script id="asciicast-RXJB9WwxwIxCRBYhdqtLLr2w6" src="https://asciinema.org/a/RXJB9WwxwIxCRBYhdqtLLr2w6.js" async></script>

E agora, para você ver tudo que foi instalado, use o comandp `graph`

<script id="asciicast-J4p21Th6fF8Ll2iwQKGQml739" src="https://asciinema.org/a/J4p21Th6fF8Ll2iwQKGQml739.js" async></script>

### Executar o seu projeto

Claro, que depois de definir e instalar suas dependencias e bibliotecas do seu projeto, você 
precisa, obviamente, executar seu script ou programa python. 

Mas como se faz isso utilizando o pipenv ?

    $ pipenv run python main.py

Sim, você precisa rodar assim pois você _não precisa estar com o ambiente virtual ativado_ sempre, como
acontece com as outras ferramentas.

Claro, se você quiser, pode *entrar* no ambiente virtual e executar os scripts de lá. 

    $ pipenv shell

### Instalação em produção

Para você executar a instalação em produção, você não precisa instalar o que foi utilizado em `dev`.

Para fazer a instalação diretamente no sistema, como quando você precisa fazer isso em um Docker por exemplo,
você utiliza o seguinte comando:

    $ pipenv install --system

Com ele, o pipenv utiliza o pip do sistema e não do virtualenv. Mas o melhor é utilizar o comando deploy,
que faz a verificação se as bibliotecas estão devidamente "locked" no arquivo Pipfile.lock e aborta se não
estiver.

Para garantir é sempre bom executar o `lock`

    $ pipenv lock

### Conclusão

E com isto, acho que conseguimos passar pelos pontos mais importantes do pipenv.

* Como criar e remover os ambientes virtuais
* Como o Pipenv gerencia as dependencias pelo Pipfile
* Como executar comandos dentro do ambiente
* Como gerenciar as libs para o ambiente de dev e de prod
* Como fazer o deploy e o lock

Ele tem outros comandos também, por exemplo, o `clean` que desinstala todas as 
biblitecas do ambiente, que não estão definidas no Pipfile. Daí só você desbravar um pouco 
mais através do `pipenv --help`.


<small>Todo este post foi baseado na documentação do Pipenv: https://pipenv.pypa.io/en/latest/</small>

<small>Terminais gravados com https://asciinema.org/</small>