import Router from 'vue-router'
import TimeReservationPage from "../page/TimeReservationPage";
import LoginPage from "../page/LoginPage";



export default new Router({
  routes: [
    {
      path: '/',
      name: 'TimeReservationPage',
      component: TimeReservationPage
    },
    {
      path: '/login',
      name: 'LoginPage',
      component: LoginPage
    }
  ]
})
