<template>
  <div>
    <timetable v-bind:days="['2019-03-30','2019-03-31']"></timetable>
    <date-time-picker v-bind:days="['2019-03-30','2019-03-31']"></date-time-picker>
  </div>
</template>

<script>

  import DateTimePicker from "../components/DateTimePicker";
  import Timetable from "../components/Timetable";

  export default {
    name: "TimeReservationPage",
    components: { DateTimePicker, Timetable },
    data() {
      return {
        startDay: '2019-03-30'
      }
    },
    computed: {

    }
  }
</script>

<style scoped>

</style>
