<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
    <v-data-table
      :headers="dayHeaders"
      :items="rows"
      :total-items="rows.length"
      hide-actions
      class="elevation-1"
    >
      <template v-slot:items="props">
        <td>{{ props.item.time }}</td>
        <template v-for="day in 7">
          <td v-html="getReservationText(findReservation(props.item.reservations, day-1))"></td>
        </template>
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
      rows: function() {
        const result = [];

        for (let time = this.startTime; time < this.endTime-1; time++) {
          let row = { time: `${time}:00~${time+1}:00` };
          row['reservations'] = this.reservations
                                    .filter(reservation => this.isTimeIn(reservation, time - this.startTime));
          result.push(row)
        }
        return result;
      }
    },
    methods: {
      findReservation: function(reservations, day) {
        let result = reservations.filter(reservation => reservation.day === day);
        return result ? result[0] : null;
      },
      getReservationText: function(reservation) {
        if (reservation) {
          return `${reservation.title} <br/> ${reservation.name}`;
        }
        return '';
      },
      isTimeIn: function(reservation, time) {
        return reservation.start_time <= time && time <= reservation.end_time;
      }
    },
    data() {
      return {
        startDate: new Date('2019-04-10'),
        startTime: 9,
        endTime: 23,
        reservations: [
          {
            "title" : "python 스터디1",
            "name" : "김수홍",
            "day" : 0,
            "start_time": 0,
            "end_time":2,
          },
          {
            "title" : "python 스터디2",
            "name" : "김수홍2",
            "day" : 0,
            "start_time": 5,
            "end_time": 5,
          },
          {
            "title" : "python 스터디3",
            "name" : "김수홍3",
            "day" : 5,
            "start_time":3,
            "end_time":4,
          },
          {
            "title" : "python 스터디4",
            "name" : "김수홍4",
            "day" : 3,
            "start_time":2,
            "end_time":3,
          }
        ]
      }
    }
  }
</script>

<style scoped>
</style>
