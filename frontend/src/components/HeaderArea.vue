<template>
  <v-layout>
    <v-flex title
            font-weight-regular
            align-content-center
            pa-4
            text-xs-left
            xs10>
      KUCC 동아리방 예약
    </v-flex>

    <v-flex pa-2>
      <v-btn v-if="isNotLoggedIn"
        to="/login">
        로그인
      </v-btn>

      <v-btn v-else
             @click="logout">
        로그아웃
      </v-btn>
    </v-flex>
  </v-layout>
</template>

<script>
  export default {
    name: "HeaderArea",
    computed: {
      isNotLoggedIn: function() {
        console.log('isNotLoggedIn ' + global.store.state.token !== null);
        return global.store.state.token === null;
      }
    },
    methods: {
      logout: function() {
        global.store.commit('removeToken');
      }
    }
  }
</script>

<style scoped>

</style>
