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
          <td class="timetable-cell"
              :style="{ height: reservationHeight*2 + 'px' }">
            <div class="timetable-cell-placeholder"></div>
            <div v-if="findReservation(props.item.reservations, day-1)"
                      class="reservation bg-blue text-center"
                      :style="getReservationStyle(findReservation(props.item.reservations, day-1))">

                {{ findReservation(props.item.reservations, day-1).title }}<br />
                {{ findReservation(props.item.reservations, day-1).name }}
            </div>
          </td>
        </template>
      </template>
    </v-data-table>
</template>

<script>
  import { getDayOfWeek, getDayString } from "../utils/dateUtil";

  function getDateHeader(date) {
    return {
      text: `${getDayString(date)} (${getDayOfWeek(date)})`,
      value: `${getDayString(date)} (${getDayOfWeek(date)})`,
      align: 'center',
      sortable: false
    };
  }

  export default {
    name: "Timetable",
    props: ['reservations', 'days'],
    computed: {
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
      getReservationStyle: function(reservation) {
        return {
          'top': reservation.start_time % 2 === 0 ? '0' : '50%',
          'height': this.reservationHeight * (reservation.end_time - reservation.start_time + 1) + 'px',
          'background-color': this.generateColor(reservation),
          'color': 'white',
        };
      },
      isTimeIn: function(reservation, time) {
        return time*2 <= reservation.start_time && reservation.start_time <= time*2 + 1;
      },
      generateColor: function(reservation) {
        return `rgba(${reservation.start_time * 10},
                     ${this.endTime - this.startTime - reservation.end_time * 10},
                     ${(8-reservation.day) * 20},
                      0.7)`
      }
    },
    data() {
      return {
        startDate: new Date(),
        reservationHeight: 35,
        startTime: 9,
        endTime: 23,
      }
    }
  }
</script>

<style scoped>
  table.v-table tbody td:not(:first-child) {
    padding: 0;
  }

  .timetable-cell {
    position: relative;
  }

  .timetable-cell-placeholder {
    width: 150px;
  }

  .reservation {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    position: absolute;
  }

  .bg-blue {
    background-color: #789DFE;
  }
</style>
