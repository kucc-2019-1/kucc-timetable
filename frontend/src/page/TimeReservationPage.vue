<template>
  <div>
    <timetable
      :reservations="reservations"
      :days="days"
    ></timetable>
    <date-time-picker v-bind:days="days"></date-time-picker>
  </div>
</template>

<script>

  import DateTimePicker from "../components/DateTimePicker";
  import Timetable from "../components/Timetable";
  import api from "../api";

  export default {
    name: "TimeReservationPage",
    components: { DateTimePicker, Timetable },
    methods: {
      loadReservations: function () {
        api.get('/reservations')
          .then(json => {
            this.reservations = json.data;
          })
          .catch(e => console.error(e));
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

</style>
