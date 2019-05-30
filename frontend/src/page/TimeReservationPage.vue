<template>
  <v-layout column>
    <header-area/>
    <v-spacer></v-spacer>
    <timetable
      :reservations="reservations"
      :days="days"
    ></timetable>
    <date-time-picker v-bind:days="days"
                      v-on:reservation-updated="loadReservations"></date-time-picker>
  </v-layout>
</template>

<script>

  import HeaderArea from "../components/HeaderArea"
  import DateTimePicker from "../components/DateTimePicker";
  import Timetable from "../components/Timetable";
  import api from "../api";

  export default {
    name: "TimeReservationPage",
    components: { DateTimePicker, Timetable, HeaderArea },
    methods: {
      loadReservations: function () {
        api.get('/reservations')
          .then(json => {
            this.reservations = json.data;
          })
          .catch(e => alert('시간표 정보를 불러오는 데 실패했습니다.'));
      }
    },
    mounted() {
      this.loadReservations();
    },
    data() {
      return {
        reservations: [],
      }
    },
    computed: {
      days: function() {
        let dayList = [];
        const startDate = new Date();
        for(let i = 0; i < 7; i++) {
          const nextDate = new Date();
          nextDate.setDate(startDate.getDate() + i);
          dayList.push(nextDate);
        }
        return dayList;
      }
    }
  }
</script>

<style scoped>
  .spacer {
    height: 40px;
  }
</style>
