<template>
  <div>
    <v-card-title class="title font-weight-regular">
      KUCC 동아리방 예약
    </v-card-title>
    <v-btn v-if="isNotLoggedIn"
      to="/login">
      로그인
    </v-btn>

    <v-btn v-else
           @click="logout">
      로그아웃
    </v-btn>
  </div>
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
