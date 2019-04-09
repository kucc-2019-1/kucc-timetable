import Vue from 'vue'
import Vuetify from 'vuetify'
import Router from 'vue-router'
import 'vuetify/dist/vuetify.min.css'
import TimeReservationPage from "../page/TimeReservationPage";

Vue.use(Router);
Vue.use(Vuetify);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'TimeReservationPage',
      component: TimeReservationPage
    }
  ]
})
