import Vue from 'vue'
import Vuetify from 'vuetify'
import Router from 'vue-router'
import HelloWorld from '@/components/DateTimePicker'
import 'vuetify/dist/vuetify.min.css'
import DateTimePicker from "../components/DateTimePicker";

Vue.use(Router)
Vue.use(Vuetify)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'DateTimePicker',
      component: DateTimePicker
    }
  ]
})
