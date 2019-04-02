<template>
  <div>
    <div id="datepicker">
      <v-select
        @change="onDayChange"
        :items="days"
        label="날짜"
      ></v-select>
    </div>
    <div id="timepicker">
      <v-checkbox
        style="height: 10px;"
        v-for="time in findTimes(currentDate)"
        :label="`${time}`"
        :value="`${time}`"
      ></v-checkbox>
    </div>
  </div>
</template>


<script>
  export default {
      name: "DateTimePicker",
      data () {
        return {
          currentDate: '',
          days: ['2019-03-30','2019-03-31'],
          dates: [
            {
              day: '2019-03-30',
              times: [
                '9:00~9:30',
                '9:30~10:00',
                '10:00~10:30',
                '10:30~11:00',
                '11:00~11:30',
                '11:30~12:00',
              ]
            },
            {
              day: '2019-03-31',
              times: [
                '9:00~9:30',
                '9:30~10:00',
                '13:00~13:30'
              ]
            }
          ]
        }
      },
      methods: {
        onDayChange: function (day) {
          this.currentDate = day;
        },
        findTimes: function (day) {
          let filteredDate = this.dates.filter(date => date.day === day);
          if  (filteredDate.length != 0) {
            return filteredDate[0].times;
          }
          return [];
        }
      },
    }
</script>

<style scoped>
  #datepicker {
    display: inline-block;
    width: 180px;
    margin-left: 30px;
    margin-right: 30px;
    float: left;
  }
  #timepicker {
    display:inline-block;
    width: 300px;
    float: left;
  }

</style>
