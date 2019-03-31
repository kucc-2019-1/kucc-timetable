<template>
    <div id="datepicker">
<!--      <v-date-picker v-model="picker" :landscape="landscape" :reactive="reactive"></v-date-picker>-->
      <v-select
        :items="days"
        label="날짜"
      ></v-select>
    </div>
</template>

<script>
    export default {
      el:'#datepicker',
      name: "DateTimePicker",
      data () {
        return {
          picker: new Date().toISOString().substr(0,10),
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
      }
    }
</script>

<style scoped>

</style>
