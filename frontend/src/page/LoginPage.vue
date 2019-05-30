<template>
  <v-layout justify-center="true">
    <v-card id="login-container">
      <v-card-title class="title font-weight-thin">
        로그인
      </v-card-title>
      <v-divider/>
      <!--<v-form class="mt-4" justify-center="true">-->
        <v-text-field v-model="username"
                      class="login-input mt-4"
                      label="아이디"></v-text-field>
        <v-text-field v-model="password"
                      class="login-input"
                      label="비밀번호"
                      type="password"></v-text-field>

        <v-btn @click="login"
               color="#A0D468"
               dark>로그인</v-btn>
      <!--</v-form>-->
    </v-card>
  </v-layout>
</template>

<script>
  export default {
    name: "LoginPage",
    data() {
      return {
        username: "",
        password: ""
      }
    },
    methods: {
      login: function() {
        if (this.username.length === 0) {
          alert('아이디를 입력해주세요');
          return;
        }

        if (this.password.length === 0) {
          alert('비밀번호를 입력해주세요');
          return;
        }

        api.post('/auth/login', {
          'username': this.username,
          'password': this.password
        }).then(body => {
          global.store.commit('updateToken', body.token);
          this.$router.push('/');
        }).catch(e => {
          console.error(e);
          alert('로그인에 실패했습니다.')
        });
      }
    }
  }
</script>

<style scoped>
  #login-container {
    width: 500px;
    height: 300px;
    padding: 20px;
  }

  .login-input {
    width: 430px;
    margin: 0 auto;
  }
</style>
