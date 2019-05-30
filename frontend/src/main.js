// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import api from './api';
import Vuex from "vuex";
import Router from "vue-router";
import 'vuetify/dist/vuetify.min.css'
import Vuetify from 'vuetify'

Vue.config.productionTip = false


Vue.use(Router);
Vue.use(Vuetify);
Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    token: localStorage.getItem('token'),
  },
  mutations: {
    updateToken(state, newToken){
      localStorage.setItem('token', newToken);
      state.token = newToken;
    },
    removeToken(state){
      localStorage.removeItem('token');
      state.token = null;
    }
  },
  actions: {
  }
});

global.store = store;
global.api = api;
global.router = router;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
