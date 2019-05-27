<template>
  <div>
    <br>
    <div id="datepicker" style ="height: 300px;" >
      <v-app id="inspire">
        <v-flex xs12 sm6 d-flex>
          <v-select
            @change="onDayChange"
            :items="days"
            :value ="days"
            v-model="selectedDay"
            id="dateValue"
            label="날짜">
          </v-select>
        </v-flex>
      </v-app>
    </div>

    <div id="timepicker">
      <div class="timepicker-section" v-for="page in getPages(findTimes(currentDate))" :key="page">
        <v-checkbox
          style="height: 10px;"
          v-model="selectedTimes"
          v-for="time in findTimes(currentDate).slice(page, page+6)"
          :key="time"
          :label="time"
          :value="time"
        ></v-checkbox>
      </div>
    </div>
     <form id="inputpurpose">
       <br>
       <input id = "purpose" type="text" name = "purpose" value="스터디명을 입력하세요" style = "outline: 1px solid"  onfocus="this.value=''">
       <button @click="onSubmitButtonClick"
         class="button" type="button" style = "outline: 2px solid">확인</button>
     </form>
    <div>{{selectedDay}}</div>
    <div>{{selectedTimes}}</div>
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
              {
                "order": 0,
                "time": "09:00 ~ 09:30"
              },
              {
                "order": 1,
                "time": "09:30 ~ 10:00"
              },
              {
                "order": 3,
                "time": "10:00 ~ 10:30"
              },
              {
                "order": 6,
                "time": "11:30 ~ 12:00"
              }
            ]
          },
          {
            day: "2019-03-31",
            times:
              [
                {
                  "order": 0,
                  "time": "09:00 ~ 09:30"
                },
                {
                  "order": 6,
                  "time": "11:30 ~ 12:00"
                }
              ]
          }
        ],
        selectedDay: "",
        selectedTimes: []
      };
    },
    methods: {
      onDayChange: function (day) {
        this.currentDate = day;
        return day;
      },
      findTimes(day) {
        let filteredDate = this.dates.filter(date => date.day === day);
        if (filteredDate.length != 0) {
          return filteredDate[0].times.map(time => time.time);
        }
        return [];
      },
      getPages(times) {
        return [...Array(Math.ceil(times.length / 6)).keys()].map(x => x * 6);
      },
      onSubmitButtonClick() {
        let data = {
          "title": document.getElementById("purpose").value,
          "name": '김가은',
          "day": this.selectedDay,
          "start_time": this.selectedTimes[0],
          "end_time": this.selectedTimes[this.selectedTimes.length-1]
        };
        console.log(data);
      }
    }
  };

</script>

<style scoped>
  #datepicker {
    display: inline-block;
    width: 300px;
    margin-left: 30px;
    margin-right: 10px;
    float: left;
    length: 300px;
  }

  #timepicker {
    display: flex;
    width: 300px;
    float: left;
  }

  #inputpurpose{
    display: inline-block;

  }
  .timepicker-section {
    margin-right: 30px;
  }

  #purpose{
    width: 300px;
    padding: 10px;
    margin-right: 30px;
    display: inline-block;
  }

  .button{
    padding: 9px;
    display: inline-block;
    background-color: darkblue;
    font-weight: bold;
    color: white;
  }
</style>
