# Web Health Monitoring (WHM)
Trabalho de Conclusão de Curso.<br>
Universidade: Fundação Herminio Ometto - Uniararas<br>
Curso: Sistemas da Informação<br>
Alunos: Higor Freitas de Oliveira e Wallace Petrucci Neves<br>
Orientador: Diego Negretto<br>
Agradecimentos e Ajuda:<br>
Orlando Saraiva, Lucas Brandani Custódio

===================================================

### Descrição do projeto
Sistema de monitoramento remoto. Sensores de Temperatura, Frequência Cardiaca e Oximetria.<br>
Projeto criado com uma placa Raspberry Pi w Zero v1.1, processando os dados dos sensores e enviando para um servidor
em cloud via Socket.<br>
Ao receber os dados o servidor dispara em evento chamado "response_front".<br>
Dentro do painel web, um socket é aberto com o servidor assinando e 'escutando' o evento "response_front", pegando os dados que o servidor dispara para o evento.

===================================================
### Pré-Requisitos.

Python3.6+
https://www.python.org/downloads/release/python-360/

Virtual Enviroment
https://robbinespu.gitlab.io/blog/2019/07/23/Python-36-with-VirtualEnv/

=====================================================

### Não tem Raspberry? - Simulando o envio de dados localmente.
Para simular o projeto geral é necessário rodar 2 scripts e o servidor local do vue.js.<br>

#### server.py<br>
script responsável por simular o servidor.<br>

1 - Abra terminal e vá até o diretório whm. Digite o comando abaixo para a instalação de dependências.
```
# pip install -r requirements.txt
```
2 - Para rodar o servidor digite:
```
# python server.py
```
<br>
Obs: O script será iniciado com um servidor local na porta 5000. Ele estará esperando algum evento ser disparado por algum cliente.
host: localhost:5000

------------------------

#### client_local.py<br>
Script responsável por enviar os dados.

1 - Digite no terminal:

```
# python client.py
```

Obs: O script será iniciado com a mensagem na tela <b>"CONNECT ON" </b>. Após isso será iniciado o laço de envio de informações. <b>Lembrando que o servidor da etapa anterior precisa estar conectado</b>

------------------------
#### Vue.JS<br>
Agora para visualizarmos os dados sendo apresentado em tempo real na página. Vamos subir o servidor local do Vue.JS.

1- Vá até a pasta /tcc/frontend

2- Confirme se existe o arquivo chamado 'package.json'.

3- Digite o comando no terminal:

``` 
# npm install
```
Será instalado automaticamente todas as dependências necessárias para rodar o projeto.

8- Execute o comando no terminal:

```
# npm run serve
```

Com esse comando irá subir o servidor local do Vue.JS, por padrão irá subir nas portas 8080. Abra seu navegador e acesse
http://localhost:8080 , irá aparecer a tela padrão do painel com os 3 cards simulando os dados dos sensores, e pegando informação em tempo real.

===================================================
