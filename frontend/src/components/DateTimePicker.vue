<template>
  <div>
    <br>
    <div id="datepicker" style ="height: 300px;" >
      <v-app id="inspire">
        <v-flex xs12 sm6 d-flex>
          <v-select
            @change="onDayChange"
            :items="dayStrings"
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
          v-for="time in findTimes(currentDate).slice(page, page+10)"
          :key="time.order"
          :label="time.time"
          :value="time.order"
        ></v-checkbox>
      </div>
    </div>
     <form id="inputpurpose">
       <br>
       <input id="purpose"
              type="text"
              name="purpose"
              placeholder="스터디명을 입력하세요"
              v-model="purpose">
       <button @click="onSubmitButtonClick"
         class="button" type="button" style = "outline: 2px solid">확인</button>
     </form>
  </div>
</template>


<script>

  export default {
    name: "DateTimePicker",
    props: ['days'],
    computed: {
      dayStrings: function() {
        return this.days.map((d) => d.toISOString().split('T')[0])
      }
    },
    data() {
      return {
        currentDate: "",
        dates: [],
        selectedDay: "",
        selectedTimes: [],
        purpose: "",
      };
    },
    methods: {
      onDayChange: function (day) {
        this.currentDate = day;
        if (this.findTimes(day).length === 0) {
          this.getReservableTimes(day);
        }
        return day;
      },
      findTimes(day) {
        let filteredDate = this.dates.filter(date => date.day === day);
        if (filteredDate.length != 0) {
          return filteredDate[0].times.map(time => time);
        }
        return [];
      },
      getReservableTimes(day) {
        //TODO 호출중에 다시 호출되지 않게 해야 함
        api.get('/times', {day: day})
          .then(body => {
            this.dates.push({
              day: day,
              times: body.data,
            })

            console.log(this.dates)
          })
          .catch(e => console.error(e))//alert('예약 가능한 시간을 불러오는 데 실패했습니다.'))
      },
      getPages(times) {
        return [...Array(Math.ceil(times.length / 10)).keys()].map(x => x * 10);
      },
      onSubmitButtonClick() {
        if (this.selectedTimes.length === 0) {
          alert('예약할 시간을 선택해주세요!')
          return;
        }

        if (this.purpose.length === 0) {
          alert('사용 목적을 입력해주세요!');
          return;
        }

        this.selectedTimes.sort();
        let data = {
          "title": this.purpose,
          "name": '김가은',
          "day": this.dayStrings.indexOf(this.selectedDay),
          "start_time": this.selectedTimes[0],
          "end_time": this.selectedTimes[this.selectedTimes.length-1]
        };
        api.post('/reservations/', data)
          .then(body => {
            this.$emit('reservation-updated');
            console.log('updated');
          }).catch(e => console.log(e));
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
    float: left;
  }

  #inputpurpose{
    display: inline-block;

  }
  .timepicker-section {
    width: 150px;
    margin-right: 30px;
  }

  #purpose{
    width: 300px;
    padding: 10px;
    margin-right: 30px;
    display: inline-block;
    outline: 1px solid;
  }

  .button{
    padding: 9px;
    display: inline-block;
    background-color: darkblue;
    font-weight: bold;
    color: white;
  }
</style>
