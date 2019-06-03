# Web Monitoring Health (WHM)
Trabalho de Concluso de Curso.<br>
Universidade: Fundação Herminio Ometto - Uniararas<br>
Curso: Sistemas da Informação<br>
Alunos: Higor Freitas de Oliveira e Wallace Petrucci Neves<br>
Orientador: Diego Negretto<br>
Agradecimentos e Ajuda:<br>
Orlando Saraiva, Lucas Brandani Custódio

### Descrição do projeto
Sistema de monitoramento remoto. Sensores de Temperatura, Frequência Cardiaca e Oximetria.<br>
Projeto criado com uma placa Raspberry Pi w Zero v1.1, processando os dados dos sensores e enviando para um servidor
em cloud via Socket.<br>
Ao receber os dados o servidor dispara eles em um evento chamado "response_front".<br>
Dentro do painel, um socket é aberto com o servidor escutando o evento "response_front", pegando os dados que o servidor dispara para o evento.

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
Obs: O script será iniciado com um servidor local na porta 5000. Ele estará esperando algum evento ser disparado por algum cliente, para apresentar algo na tela.
host: localhost:5000

<br><br>
#### client.py<br>
Script responsável por enviar os dados.

1 - Para conseguir acessar o servidor será preciso identificar para qual HOST:PORT o cliente está enviando informações, acesse o arquivo client.py com algum editor de sua preferẽncia e procure a linha onde tenha:<br>
```
socketobj = SocketWhm(const.HOST, const.PORT)
```
- Mude a constante const.HOST para const.HOST_LOCAL
- Mude a constante const.PORT para const.PORT_LOCAL
- Salve o arquivo

2 - Para rodar o cliente, digite no terminal:
```
# python client.py
```

Obs: O script será iniciado com a mensagem na tela <b>"CONNECT ON" </b>. Após isso será iniciado o laço de envio de informações
