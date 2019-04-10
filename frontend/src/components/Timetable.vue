<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
    <v-data-table
      :headers="dayHeaders"
      :items="times"
      :total-items="times.length"
      hide-actions
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
      text: `${date.toISOString().split('T')[0]} (${getDayOfWeek(date)})`,
      value: `${date.toISOString().split('T')[0]} (${getDayOfWeek(date)})`,
      align: 'center',
      sortable: false
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
          text: '시간',
          value: 'time',
          align: 'center',
          sortable: false
        }];
        return header.concat(this.days.map(getDateHeader));;
      },
      times: function() {
        const result = [];

        for (let time = this.startTime; time < this.endTime-1; time++) {
          result.push({time: `${time}:00~${time+1}:00`})
        }
        return result;
      }
    },
    data() {
      return {
        startDate: new Date('2019-04-10'),
        startTime: 9,
        endTime: 23,
      }
    }
  }
</script>

<style scoped>
</style>
