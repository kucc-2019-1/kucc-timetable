<template>
  <div id="datepicker">
    <v-select
      @change="changedLabel"
      :items="days"
      label="날짜"
    ></v-select>
    <div id="timepicker">
      <v-checkbox
        v-for="time in dates[0].times"
        :label="`${time}`"
        :value="`${time}`"
      ></v-checkbox>
      <v-checkbox
        v-for="time in dates[1].times"
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
          landscape: false,
          reactive: false,
          days: ['2019-03-30','2019-03-31'],
          dates: [
            {
              day: '2019-03-30',
              times: [
                '9:00~9:30',
                '9:30~10:00'
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
        changedLabel: function (event) {
          alert(event)
        }
      },
    }
</script>

<style scoped>
  #datepicker {
    width: 20%;
  }
</style>
