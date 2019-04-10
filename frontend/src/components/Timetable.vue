<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
    <v-data-table
      :headers="dayHeaders"
      :items="times"
      :total-items="times.length"
      :hide-actions="false"
      class="elevation-1"
    >
      <template v-slot:items="props">
        <td>{{ props.item.time }}</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
      </template>
    </v-data-table>
</template>

<script>
  import { getDayOfWeek } from "../utils/dateUtil";

  function getDateHeader(date) {
    return {
      'text': `${date.toISOString().split('T')[0]} (${getDayOfWeek(date)})`,
      'value': `${date.toISOString().split('T')[0]} (${getDayOfWeek(date)})`,
      'align': 'center',
      'sortable': false
    };
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
        return dayList;
      },
      dayHeaders: function() {
        const header = [{
          'text': '시간',
          'value': 'time',
          'align': 'center',
          'sortable': false
        }];
        return header.concat(this.days.map(getDateHeader));;
      }
    },
    data() {
      return {
        startDate: new Date('2019-04-10'),
        times: [
          { 'time': '9:00~9:30'  },
          { 'time': '9:30~10:00' },
          { 'time': '10:00~10:30' },
          { 'time': '10:30~11:00' },
          { 'time': '11:00~11:30' },
          { 'time': '11:30~12:00' },
          { 'time': '12:00~12:30' },
          { 'time': '12:30~13:00' },
          { 'time': '13:00~13:30' },
          { 'time': '13:30~14:00' },
          { 'time': '14:00~14:30' },
          { 'time': '14:30~15:00' },
          { 'time': '15:00~15:30' },
          { 'time': '15:30~16:00' },
          { 'time': '16:00~16:30' },
          { 'time': '16:30~17:00' },
          { 'time': '17:00~17:30' },
          { 'time': '17:30~18:00' },
          { 'time': '18:00~18:30' },
          { 'time': '18:30~19:00' },
          { 'time': '19:00~19:30' },
          { 'time': '19:30~20:00' },
          { 'time': '20:00~20:30' },
          { 'time': '20:30~21:00' },
          { 'time': '21:00~21:30' },
          { 'time': '21:30~22:00' },
          { 'time': '22:00~22:30' },
          { 'time': '22:30~23:00' }
        ]
      }
    }
  }
</script>

<style scoped>
  /*table {*/
  /*  border-collapse: collapse;*/
  /*}*/
  /*th, td {*/
  /*  padding: 3px;*/
  /*  border: 1px solid black;*/
  /*  border-spacing: 0px;*/
  /*}*/
</style>
