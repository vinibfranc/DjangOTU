# DjangOTU

Esse projeto é um teste para vaga na Neoprospecta, incluindo exibição e filtragem do conteúdo de uma OTU table resultante de dados sequenciamento do marcador de bactérias 16s em amostras de fezes de camundongos, objetivando investigar as variações na microbiota intestinal em diferentes dias após o desmame dos animais.

---------------------------------------

Para a etapa 3 deste desafio foram utilizadas as seguintes linguagens de programação, ferramentas e bibliotecas principais:

- [Python3](https://www.python.org/download/releases/3.0/) (v3.6.8)
- [Django framework](https://www.djangoproject.com/) (v.3.0.3)
- [pandas](https://pandas.pydata.org/) (v.0.1)
- [HTML5](https://developer.mozilla.org/pt-BR/docs/Web/HTML/HTML5)
- [CSS3](https://developer.mozilla.org/pt-BR/docs/Archive/CSS3)
- [Java Script](https://www.javascript.com/)
- [Bootstrap](https://getbootstrap.com/) (v. 4.4)
- [DataTables](https://datatables.net/) (v1.10.20)

## Execução local do site 

Para executar o site localmente, algumas etapas precisam ser feitas para ter nosso ambiente configurado. Os comandos de instalação abaixo foram executados no Ubuntu 18.04, caso seu sistema operacional não for compatível, procure como instalar tais programas.

1. Instalar Python3 e pip:

```
$ sudo apt-get install python3
$ sudo apt-get install python3-pip
```

2. Criar uma pasta e colocar o código-fonte da aplicação, que está hospedado no GitHub, dentro dela:

```
$ mkdir <nome_pasta>
$ cd <nome_pasta>
$ git clone https://github.com/vinibfranc/DjangOTU
```

3. Com o código-fonte, podemos navegar para a pasta que o contém:

```
$ cd DjangOTU/
```

4. Agora, iremos instalar e configurar uma virtual environment (virtualenv) para a aplicação:

```
$ pip3 install virtualenv
```

Com isso, podemos verificar onde o Python foi instalado para fazer a virtualenv apontar para eles:

```
$ which python3
/usr/bin/python3
```

Então podemos criar o diretório da virtualenv dentro do nosso projeto:

```
$ mkdir venv/
$ cd venv
```

Finalmente, podemos criar a nossa virtualenv para o projeto, passando como parâmetro o resultado do comando ```which python3``` feito acima:

```
$ virtualenv . -p /usr/bin/python3
```

O último passo agora, e sempre que formos trabalhar no projeto, é voltar para a pasta ```DjangOTU``` e ativar a virtualenv:

```
$ cd ..
$ source venv/bin/activate
```

5. Agora, com nosso ambiente ativo, podemos finalmente instalar o Django e as dependências do projeto:

```
(venv) $ pip3 install -r requirements.txt
```

Pronto! Todas as configurações foram feitas e o site já pode ser acessado.

------------------------------

## Navegação no site

Para iniciar a aplicação, navegamos para a pasta do projeto e rodamos o comando:

```
(venv) $ cd project
(venv) $ python3 manage.py runserver
```

Podemos abrir esse site no browser no endereço [http://127.0.0.1:8000/](http://127.0.0.1:8000/), ou então clicar com o mouse e o shift pressionado no terminal onde aparecerá a mensagem ```Starting development server at http://127.0.0.1:8000/```.

Ao abrir a página teremos uma página Home, feita essencialmente com HTML e Bootstrap, justamente para dar uma visão geral sobre o propósito deste site. 

Em seguida, podemos acessar a nossa OTU table. Ao clicar no segundo link do menu, somos direcionados para a página do Django admin, pois ainda não estamos logados.

Conforme solicitado, há um usuário criado com as seguintes credenciais:

```
usuário: neoprospecta
senha: neopct1234
```

Ao logar com esse usuário, por padrão somos direcionados ao nosso perfil na área administrativa do Django. Para voltar à OTU table, podemos acessar a URL [http://127.0.0.1:8000/otu_table/](http://127.0.0.1:8000/otu_table/), ou então reabrir a página inicial e clicar no link da OTU table. 

Nessa tela, teremos acesso à OTU table, que foi carregada como uma tabela HTML em uma View do Django utilizando a biblioteca pandas. Em seguida essa tabela foi estilizada utilizando o Bootstrap 4. Finalmente, foi utilizado um plugin para a biblioteca do Jquery, chamado DataTables.js, para permitir a exibição da quantidade de linhas desejadas pelo usuário, a paginação dos dados, a pesquisa de OTUs específicas, bem como a ordenação dos dados por OTUs e frequências. Para fazer as filtragens, basta clicar na coluna ao qual você deseja ordenar. Caso queira ordenar múltiplas colunas de uma só vez, segura a tecla Shift e clicar sobre as colunas de interesse.

## Autor

Desenvolvido por [Vinícius Franceschi](https://vinibfranc.github.io/) - Bacharel em Informática Biomédica (UFCSPA).

Dúvidas, problemas encontrados ou sugestões de melhorias podem ser enviadas para: vinibfranc@gmail.com
