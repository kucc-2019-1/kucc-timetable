<template>
  <div>
    <div id="datepicker">
      <v-select @change="onDayChange" :items="days" label="날짜"></v-select>
    </div>
    <div id="timepicker">
      <div class="timepicker-section" v-for="page in getPages(findTimes(currentDate))" :key="page">
        <v-checkbox
          style="height: 10px;"
          v-for="time in findTimes(currentDate).slice(page, page+6)"
          :key="time"
          :label="time"
          :value="time"
        ></v-checkbox>
      </div>
    </div>
  </div>
</template>


<script>
  export default {
    name: "DateTimePicker",
    data() {
      return {
        currentDate: "",
        days: ["2019-03-30", "2019-03-31"],
        dates: [
          {
            day: "2019-03-30",
            times: [
              "9:00~9:30",
              "9:30~10:00",
              "10:00~10:30",
              "10:30~11:00",
              "11:00~11:30",
              "11:30~12:00",
              "12:00~12:30",
              "12:30~13:00"
            ]
          },
          {
            day: "2019-03-31",
            times: [
              "9:00~9:30",
              "9:30~10:00",
              "13:00~13:30"]
          }
        ]
      };
    },
    methods: {
      onDayChange(day) {
        this.currentDate = day;
      },
      findTimes(day) {
        let filteredDate = this.dates.filter(date => date.day === day);
        if (filteredDate.length != 0) {
          return filteredDate[0].times;
        }
        return [];
      },
      getPages(times) {
        return [...Array(Math.ceil(times.length / 6)).keys()].map(x => x * 6);
      }
    }
  };
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
    display: flex;
    width: 300px;
    float: left;
  }

  .timepicker-section {
    margin-right: 30px;
  }
</style>
