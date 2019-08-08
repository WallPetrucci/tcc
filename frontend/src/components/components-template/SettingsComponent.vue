<template>
  <v-card class="elevation-12">
    <v-toolbar dark color="primary">
      <v-toolbar-title>{{currentTitle}}</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-tooltip bottom>
        <template v-slot:activator="{ on }">
          <v-btn icon large target="_blank" v-on="on" @click="displayRegisterMethod()">
            <v-icon>fas fa-user-plus</v-icon>
          </v-btn>
        </template>
        <span>Novo Cadastro</span>
      </v-tooltip>
    </v-toolbar>
    <template>
      <v-window v-model="step">
        <v-window-item :value="1">
          <v-card-text>
            <v-form>
              <v-text-field prepend-icon="person" name="login" label="Email" type="text"></v-text-field>
              <v-text-field
                id="password"
                prepend-icon="lock"
                name="password"
                label="Senha"
                type="password"
              ></v-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" class="esqueceusenha" @click="abrirEsqueciSenha()">
              Esqueceu a Senha
              <v-icon
                style="font-size: 13px; top:-1px; position:relative;margin-left:5px"
              >fas fa-question</v-icon>
            </v-btn>
            <v-btn color="primary">Acessar</v-btn>
          </v-card-actions>
        </v-window-item>
        <v-window-item :value="2">
          <v-card-text>
            <v-text-field label="Email" value></v-text-field>
          </v-card-text>
        </v-window-item>

        <v-window-item :value="3">
          <v-card-text>
            <v-text-field label="Senha" type="password"></v-text-field>
            <v-text-field label="Confirmar Senha" type="password"></v-text-field>
            <span class="caption grey--text text--darken-1">Entre com sua senha</span>
          </v-card-text>
        </v-window-item>

        <v-window-item :value="4">
          <v-card-text>
            <v-text-field label="Nome Completo" required></v-text-field>
            <v-menu
              ref="menu"
              v-model="menu"
              :close-on-content-click="false"
              :nudge-right="40"
              lazy
              transition="scale-transition"
              offset-y
              full-width
              min-width="290px"
              max-heigth="100px"
            >
              <template v-slot:activator="{ on }">
                <v-text-field v-model="date" label="Data de Nascimento" readonly v-on="on"></v-text-field>
              </template>
              <v-date-picker
                ref="picker"
                v-model="date"
                :max="new Date().toISOString().substr(0, 10)"
                min="1950-01-01"
                @change="save"
              ></v-date-picker>
            </v-menu>
            <v-text-field label="Telefone" placeholder="(99) 9999-9999" mask="(##) ####-####"></v-text-field>
            <v-text-field label="Celular" placeholder="(99) 99999-9999" mask="(##) ####-#####"></v-text-field>
            <span class="caption grey--text text--darken-1">Insira seus Dados Pessoais</span>
          </v-card-text>
        </v-window-item>

        <v-window-item :value="5">
          <div class="pa-3 text-xs-center">
            <v-icon>fas fa-check-circle</v-icon>
            <h3 class="title font-weight-light mb-2">Seja bem vindo!</h3>
            <span class="caption grey--text">Cadastro efetuado com sucesso</span>
          </div>
        </v-window-item>

        <v-window-item :value="6">
          <div class="pa-3 text-xs-center">
            <v-card-text>
              <v-text-field label="Email" value></v-text-field>
            </v-card-text>
            <span
              class="caption grey--text"
            >Verifique sua caixa de entrada, e clique no link informado.</span>
          </div>
        </v-window-item>
      </v-window>

      <v-divider></v-divider>

      <v-card-actions v-if="step > 1">
        <v-btn :disabled="step === 1 || step === 5" flat @click="step--" v-if="step !== 6">Voltar</v-btn>
        <v-btn v-if="step === 6" flat @click="step = 1">Voltar</v-btn>
        <v-spacer></v-spacer>
        <v-btn color="primary" depressed @click="step++" v-if="step < 4">Avançar</v-btn>
        <v-btn color="primary" @click="registerUser()" v-if="step == 4">Cadastrar</v-btn>
        <v-btn color="primary" @click="enviarEsqueceuSenha()" v-if="step == 6">Enviar</v-btn>
      </v-card-actions>
    </template>
  </v-card>
</template>
</v-card>	
</template>
<script type="text/javascript">
export default {
  name: "SettingsComponent",
  data: () => ({
    step: 1,
    displayRegister: false,
    date: null,
    menu: false
  }),
  mounted() {
    this.displayRegister = false;
  },
  computed: {
    currentTitle() {
      switch (this.step) {
        case 1:
          return "Painel de Acesso";
        case 2:
          return "Registrar";
        case 3:
          return "Registrar";
        case 4:
          return "Registrar";
        case 6:
          return "Recuperar a senha";
        default:
          return "Registrado com Sucesso";
      }
    }
  },
  watch: {
    menu(val) {
      val && setTimeout(() => (this.$refs.picker.activePicker = "YEAR"));
    }
  },
  methods: {
    displayRegisterMethod() {
      this.step = 2;
      this.displayRegister = true;
    },
    abrirEsqueciSenha() {
      this.step = 6;
    },
    registerUser() {
      this.step = 4;
    },
    save(date) {
      var split = date.split("-");
      var reversed = split.reverse();
      var datereverse = reversed.join("-");
      this.date = datereverse;
      this.$refs.menu.save(datereverse);
    }
  }
};
</script>