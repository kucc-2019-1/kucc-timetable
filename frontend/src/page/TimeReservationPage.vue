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

  export default {
    name: "TimeReservationPage",
    components: { DateTimePicker, Timetable },
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
