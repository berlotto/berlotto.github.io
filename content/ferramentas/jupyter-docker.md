Title: Como executar um ambiente Jupyter em um docker localmente
Date: 2021-02-21 13:00
Category: data-science
Tags: editores, codigo, notebook, jupyter
Slug: como-instalar-juoyter-notebook-no-docker
Authors: Sérgio Berlotto
Summary: Trabalhe como um cientista de dados profissional no seu computador local facilmente!
Headline: Saiba como executar um ambiente completo e muito útil
Header_Cover: static/posts/jupyter.jpg

Trabalhe como um cientista de dados profissional no seu computador local facilmente!

# Jupyter

Jupyter é um ambiente muito prático que roda os tais "notebooks", que nada mais são do 
que documentos definidos por células que contém código de executável ou markdown para 
documentação.

Não é necessário explicar muito sobre como o ambiente funciona, até mesmo pq muito
se fala sobre os tais notebooks e o Jupyter.

Mas, para diversificar um pouco, tendo os kernels instalados, conseguimos rodar não
só Python, mas Julia e R também, e se quiser dar uma olhadinha em mais opções
segue (este link)[https://github.com/jupyter/jupyter/wiki/Jupyter-kernels] e se aventura.

Isso mesmo! Inclusive, o passo-a-passo que você vai acompanhar logo abaixo irá 
lhe conduzir a ter um ambiente contendo que rode Python, R e Julia também.

## Docker

Bom, como muita aplicação hoje em dia, rodar o Jupyter é muito fácil por
conta do Docker. 

Tenha em mente que é necessário ter o docker instalado em sua máquina.

No Windowsvocê consegue instalar o Docker Desktop e no linux, diretamente pelo 
terminal.

## Imagens disponíveis

Bom, em se tratando de data-science, temos muuuuitas opções e direções. 

Podemos falar de gestão/ingestão de dados, de conhecimento de dados, de big data, de 
machine learning, de visão computacional, etc, etc, etc...

O projeto do Jupyter conhece bem seu eleitorado, e já disponibilizou uma séria de 
imagens docker que são muito bem organizadas e pré-instaladas para que possamos 
só rodar o container e sair trabalhando.

O projeto que vamos conhecer é este: https://jupyter-docker-stacks.readthedocs.io

Vamos dar uma olhadinha nas opções rapidamente para você saber qual imagem você irá ]escolher:

* jupyter/base-notebook
    * O mininmo necessário para rodar os notebooks, sem bibliotecas
* jupyter/minimal-notebook
    * Tudo que tem no base, mais algumas ferramentas, como git, vim, etc.
* jupyter/r-notebook
    * Tudo que tem no minimal, mais o ambiente do R e várias bibliotecas
* jupyter/scipy-notebook
    * Tudo que tem no minimal, mais várias bibliotecas de ciência de dados, scipy, scikit-learn, etc.
* jupyter/tensorflow-notebook
    * Tudo que tem no scipy mais Tensorflow e Keras
* jupyter/datascience-notebook
    * Tudo que tem no scipy e r mais o ambiente Julia 
* jupyter/pyspark-notebook
    * Tudo que tem no scipy mais Apache Spark
* jupyter/all-spark-notebook
    * Tudo que tem no pyspark mais suporte para Scala

![Diagrama das imagens](http://interactive.blockdiag.com/image?compression=deflate&encoding=base64&src=eJyFzTEPgjAQhuHdX9Gws5sQjGzujsaYKxzmQrlr2msMGv-71K0srO_3XGud9NNA8DSfgzESCFlBSdi0xkvQAKTNugw4QnL6GIU10hvX-Zh7Z24OLLq2SjaxpvP10lX35vCf6pOxELFmUbQiUz4oQhYzMc3gCrRt2cWe_FKosmSjyFHC6OS1AwdQWCtyj7sfh523_BI9hKlQ25YdOFdv5fcH0kiEMA)

## Executando

Bom, agora que já temos ideia de qual imagem queremos iniciar, vamos fazer o que temos
que fazer.

Lembrando que, apesar das imagens terem um propósito e terem já algumas libs instaladas
, em todas elas você consegue customizar o ambiente conforme seu desejo. 

O notebook tem dois modos de ser executado: O classico e o lab

* o lab: é uma versão mais nova, com novos recursos e mais opções de trabalho que o classic, possibilita trabalhar com abas e mais de um notebook por vez.
* o classic: é a versão mais antiga com menos recursos, e uma visão de 1 notebook só por vez.

Vamos executar o lab, e para isso necessita passar um parametro: JUPYTER_ENABLE_LAB=yes

    docker run -d --name jupyterserver -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes jupyter/datascience-notebook 

Outro detalhe é que por padrão a porta do jupyter server é 8888, o que geralmente não é 
ruim, então vamos utilizar esta porta mesmo. Mas nas configurações tem como trocar 
isso, entre outras opções também.

Executando o comando acima, você será capaz de acessar o notebook pelo seu browser na
porta 8888: http://localhost:8888

Mas, será necessário informar um token que é gerado pelo servidor, para poder acessá-lo.
Para você poder ver e acessar esse token, você pode executar um comandinho para ver o 
log do seu container e assim poder clicar no link para abrir no browser.

    docker logs --tail=50 jupyterserver

Mas, para facilitar e, se você está executando o servidor no seu computador e não necessita de segurança, você pode inibir os dois métodos de segurança que tem, que é o
token e a senha, com este comando:

    docker run -d --name jupyterserver -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes jupyter/datascience-notebook start-notebook.sh --NotebookApp.password=''  --NotebookApp.token=''

E por último, eu recomendo que você configura uma pasta local no seu computador (por 
exemplo /home/meu-user/notebooks) para que todo seu trabalho não fique apenas dentro do 
container e muito difícil de obter
depois. Então, utilizamos o volume do docker para essa tarefa.

    $ docker run -d \
        --name jupyterserver \
        -p 8888:8888 \
        -v /home/meu-user/notebooks:/home/jovyan/work \
        -e JUPYTER_ENABLE_LAB=yes \
        jupyter/datascience-notebook \
        start-notebook.sh --NotebookApp.password='' --NotebookApp.token=''

Assim, facilmente, acessando seu browser, sem a necessitade de senhas ou tokens, você
terá um ótimo ambiente para executar seus treinamentos de código, apreder mais sobre
machine learning, data-science, com Python, R ou Julia!

### Conclusão

Facilmente você tem um ambiente muito prático e configurável para poder estudar 
seus conteúdos e seus dados.

Desbrave e utilize bastante este ambiente que é muito rico

Bom trabalho!