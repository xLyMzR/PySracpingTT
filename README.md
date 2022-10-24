# PySrcapingTT
Uma pequena demonstração para treinamento utilizando biblioteca de scraping para o twitter e utilizando panda para visualização dos dados

## Scraping ##

Utilizado a biblioteca "snscrap" para realizar o scraping
de dados do Twitter.

Link Para Acesso: 
- https://github.com/JustAnotherArchivist/snscrape

_OBS_:

- Foi imposto um limite de 3000 tweets por usuario

- As requisições para a bibliote foram feitas isoladamente por usuário

- Os anos filtrados na coleta estão entre: {2016 - 2022}

- Todos os usuarios foram traçados previamente e seus nomes de usuario colocados em arquivo txt.

## Data Processing ##

Para o tratamento dos dados coletados do twitter,
Foi utilizado a biblioteca Pandas com a finalidade de
gerar arquvios csv para posteriormente trata-los e filtra-los
por data e frequência, gerando novos arquivos tratados que foram
utilizados na visualização dos dados.

Link Para Acesso:

- https://pandas.pydata.org/


## Data View ##

Para geração dos gráficos em barras (Frequência de Tweets por ano)
Foi utilizado a biblioteca  matplotlib utilizando o modulo:
pyplot para transformar DataFrames do pandas em gráficos
e posteriormente salva-los em arquivo png

Link acesso:
- https://matplotlib.org/3.5.1/api/matplotlib_configuration_api.html


- https://matplotlib.org/stable/tutorials/introductory/pyplot.html

_Exemplo Data View :_

![graphic-anacruzzs](https://user-images.githubusercontent.com/91917320/197568326-a0f1d65f-9098-4ef0-bc58-1a7f1bca0365.png)


