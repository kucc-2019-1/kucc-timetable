<template>
    <table>
      <tr>
        <th></th>
        <th v-for="day in dayHeaders">
          {{ day }}
        </th>
      </tr>
      <tr v-for="time in times">
        <td>{{ time }}</td>
        <td v-for="i in 7"></td>
      </tr>
    </table>
</template>

<script>
  import { getDayOfWeek } from "../utils/dateUtil";

  function getDateHeader(date) {
    return `${date.toISOString().split('T')[0]} (${getDayOfWeek(date)})`;
  }

  export default {
    name: "Timetable",
    computed: {
      days: function() {
        let dayList = [];
        for(let i = 0; i < 7; i++) {
          const nextDate = new Date();
          nextDate.setDate(this.startDate.getDate() + i);
          dayList.push(nextDate);
        }
        console.log(dayList);
        return dayList;
      },
      dayHeaders: function() {
        return this.days.map(getDateHeader);
      }
    },
    data() {
      return {
        startDate: new Date('2019-04-10'),
        times: [
          '9:00~9:30',
          '9:30~10:00',
          '10:00~10:30',
          '10:30~11:00',
          '11:00~11:30',
          '11:30~12:00',
          '12:00~12:30',
          '12:30~13:00',
          '13:00~13:30',
          '13:30~14:00',
          '14:00~14:30',
          '14:30~15:00',
          '15:00~15:30',
          '15:30~16:00',
          '16:00~16:30',
          '16:30~17:00',
          '17:00~17:30',
          '17:30~18:00',
          '18:00~18:30',
          '18:30~19:00',
          '19:00~19:30',
          '19:30~20:00',
          '20:00~20:30',
          '20:30~21:00',
          '21:00~21:30',
          '21:30~22:00',
          '22:00~22:30',
          '22:30~23:00',
        ]
      }
    }
  }
</script>

<style scoped>
  table {
    border-collapse: collapse;
  }
  th, td {
    padding: 3px;
    border: 1px solid black;
    border-spacing: 0px;
  }
</style>
