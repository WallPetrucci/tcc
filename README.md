# Web Monitoring Health (WHM)
Trabalho de Concluso de Curso.<br>
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
Ao receber os dados o servidor dispara eles em um evento chamado "response_front".<br>
Dentro do painel, um socket é aberto com o servidor escutando o evento "response_front", pegando os dados que o servidor dispara para o evento.

===================================================

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

#### client.py<br>
Script responsável por enviar os dados.

1 - Para conseguir acessar o servidor será preciso identificar para qual HOST:PORT o cliente está enviando informações, acesse o arquivo client.py com algum editor de sua preferẽncia e procure a linha onde tenha:<br>
```
socketobj = SocketWhm(const.HOST, const.PORT)
```
- Mude a constante const.HOST para const.HOST_LOCAL
- Mude a constante const.PORT para const.PORT_LOCAL

2 - Agora vamos remover no cdigo as chamadas para os pacotes do raspberry, como  uma simulação sem a placa, então no será necessário eles.

*Remova ou comente essa linha.
```
from temp import MLX90614
```

*Remova ou comente essa linha.
```
sensor_temperatura = MLX90614()
```

* Neste bloco de código altere somente o cóigo "sensor_temperatura.get_obj_temp" para "random.randrange(35, 39)" , ficará assim:
```
sio.start_background_task(socketobj.send_message({'whm_id': "09123901823902",
                                                              'fc': random.randrange(60, 120),
                                                              'ox': random.randrange(96, 100),
                                                              'temp': random.randrange(35, 39),
                                                              'date': current_date.strftime('%d/%m/%Y %H:%M')}))
```



3 - Pronto, após as alteraçes para rodar o cliente, digite no terminal:

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
4- acesse a pasta /tcc/frontend/src
5- Abra o arquivo main.js com seu editor de preferência.
6- Na linha abaixo troque o servidor '34.232.109.146', para 'localhost' ficando assim:
```
const SocketInstance = io.connect('http://localhost:5000');
```

7- Salve o arquivo e volte para a pasta 'frontend'
8- Execute o comando no terminal:
```
# npm run serve
```
Com esse comando irá subir o servidor local do Vue.JS, por padrão irá subir nas portas 8080. Abra seu navegador e acesse
http://localhost:8080 , irá aparecer a tela padrão do painel com os 3 cards simulando os dados dos sensores, e pegando informação em tempo real.

===================================================
